const fs = require("fs");
const path = require("path");
const os = require("os");
const { spawnSync } = require("child_process");

const ROOT = process.cwd();
const CONTENT_DIR = path.join(ROOT, "content");
const FENCE_REGEX = /```python\n([\s\S]*?)\n```/g;
const NON_RUNNABLE_REGEX = /^\s*#\s*non-runnable\b/im;
const REPL_PROMPT_REGEX = /^\s*>>>/m;
const INPUT_CALL_REGEX = /\binput\s*\(/;
const STATE_DEPENDENCY_REGEX = /NameError|UnboundLocalError/;
const CONTEXT_WINDOW = 8;
const PYTHON_TIMEOUT_MS = 10000;

function getFilesRecursive(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      getFilesRecursive(fullPath, out);
    } else if (entry.isFile() && fullPath.endsWith(".md")) {
      out.push(fullPath);
    }
  }
  return out;
}

function toRelative(filePath) {
  return path.relative(ROOT, filePath).replace(/\\/g, "/");
}

function runPythonInline(code, cwd) {
  return spawnSync("python3", ["-c", code], {
    encoding: "utf8",
    timeout: PYTHON_TIMEOUT_MS,
    cwd,
  });
}

function runPythonScript(script, cwd) {
  const tempFilePath = path.join(
    cwd,
    `py-snippet-${Date.now()}-${Math.random().toString(36).slice(2)}.py`
  );

  try {
    fs.writeFileSync(tempFilePath, script, "utf8");
    return spawnSync("python3", [tempFilePath], {
      encoding: "utf8",
      timeout: PYTHON_TIMEOUT_MS,
      cwd,
    });
  } finally {
    if (fs.existsSync(tempFilePath)) {
      fs.unlinkSync(tempFilePath);
    }
  }
}

function shouldUseForContext(code) {
  if (!code || !code.trim()) {
    return false;
  }
  if (NON_RUNNABLE_REGEX.test(code)) {
    return false;
  }
  if (REPL_PROMPT_REGEX.test(code)) {
    return false;
  }
  if (INPUT_CALL_REGEX.test(code)) {
    return false;
  }
  return true;
}

function normalizeError(result) {
  const stderr = (result.stderr || "").trim();
  if (stderr) {
    const lines = stderr.split(/\r?\n/);
    return lines[lines.length - 1];
  }

  if (result.error) {
    return result.error.message || String(result.error);
  }

  return "Unknown Python execution error";
}

function createSandboxDir() {
  return fs.mkdtempSync(path.join(os.tmpdir(), "py-snippet-sandbox-"));
}

function cleanupSandboxDir(dirPath) {
  if (!dirPath) {
    return;
  }
  try {
    fs.rmSync(dirPath, { recursive: true, force: true });
  } catch (_err) {
    // Ignore sandbox cleanup failures.
  }
}

function main() {
  if (!fs.existsSync(CONTENT_DIR)) {
    console.log("Python snippet checks skipped: content directory does not exist.");
    return;
  }

  const files = getFilesRecursive(CONTENT_DIR).sort();
  const errors = [];
  const sandboxDir = createSandboxDir();

  try {
    for (const filePath of files) {
      const source = fs.readFileSync(filePath, "utf8");
      const blocks = [];

      let match = FENCE_REGEX.exec(source);
      while (match) {
        blocks.push(match[1]);
        match = FENCE_REGEX.exec(source);
      }

      for (let index = 0; index < blocks.length; index += 1) {
        const code = blocks[index];
        const blockNumber = index + 1;

        if (NON_RUNNABLE_REGEX.test(code)) {
          continue;
        }

        if (REPL_PROMPT_REGEX.test(code)) {
          errors.push(
            `${toRelative(filePath)}#${blockNumber} uses REPL prompts (>>>). Use \`pycon\` fence instead of \`python\`.`
          );
          continue;
        }

        let execution = runPythonInline(code, sandboxDir);
        if (execution.error && execution.error.code === "ENOENT") {
          cleanupSandboxDir(sandboxDir);
          console.error("Python snippet checks failed: python3 is not available in this environment.");
          process.exit(1);
        }

        if (execution.status === 0) {
          continue;
        }

        const stderrText = `${execution.stderr || ""}${execution.error ? `\n${execution.error.message}` : ""}`;
        if (!STATE_DEPENDENCY_REGEX.test(stderrText)) {
          errors.push(`${toRelative(filePath)}#${blockNumber} failed: ${normalizeError(execution)}`);
          continue;
        }

        const contextStart = Math.max(0, index - CONTEXT_WINDOW);
        const contextBlocks = [];
        for (let i = contextStart; i < index; i += 1) {
          const candidate = blocks[i];
          if (shouldUseForContext(candidate)) {
            contextBlocks.push(candidate);
          }
        }

        const combinedSource = [...contextBlocks, code].join("\n\n");
        execution = runPythonScript(combinedSource, sandboxDir);

        if (execution.status !== 0) {
          errors.push(
            `${toRelative(filePath)}#${blockNumber} failed even with local context: ${normalizeError(execution)}`
          );
        }
      }
    }
  } finally {
    cleanupSandboxDir(sandboxDir);
  }

  if (errors.length > 0) {
    console.error("Python snippet checks failed:");
    for (const error of errors) {
      console.error(`- ${error}`);
    }
    process.exit(1);
  }

  console.log("Python snippet checks passed.");
}

main();
