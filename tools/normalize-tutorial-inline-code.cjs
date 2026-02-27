const fs = require("fs");
const path = require("path");

const ROOT = process.cwd();
const TUTORIAL_DIRS = [
  path.join(ROOT, "content", "en", "tutorial"),
  path.join(ROOT, "content", "uz", "tutorial"),
];

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

function splitFrontMatter(content) {
  if (!content.startsWith("---\n")) {
    return { frontMatter: "", body: content };
  }

  const endIndex = content.indexOf("\n---\n", 4);
  if (endIndex === -1) {
    return { frontMatter: "", body: content };
  }

  return {
    frontMatter: content.slice(0, endIndex + 5),
    body: content.slice(endIndex + 5),
  };
}

function replaceOutsideInlineCode(line, replacer) {
  const parts = line.split(/(`[^`]*`)/g);
  return parts
    .map((part, index) => (index % 2 === 1 ? part : replacer(part)))
    .join("");
}

function normalizeProseChunk(chunk) {
  let next = chunk;

  const replacements = [
    [/\bif\s*\/\s*else\b/g, "`if`/`else`"],
    [/\bif\s*-\s*else\b/g, "`if`-`else`"],
    [/\bif\s+else\b/g, "`if` `else`"],
    [/\bIf\s+else\b/g, "`if` `else`"],
    [/\bif\s+elif\b/g, "`if` `elif`"],
    [/\bIf\s+elif\b/g, "`if` `elif`"],
    [/\bif\s+condition\b/g, "`if` condition"],
    [/\bIf\s+condition\b/g, "`if` condition"],
    [/\bif\s+statement\b/g, "`if` statement"],
    [/\bIf\s+statement\b/g, "`if` statement"],
    [/\belif\s+condition\b/g, "`elif` condition"],
    [/\bfor\s+loop\b/g, "`for` loop"],
    [/\bFor\s+loop\b/g, "`for` loop"],
    [/\bfor\s+Loop\b/g, "`for` loop"],
    [/\bFor\s+Loop\b/g, "`for` loop"],
    [/\bwhile\s+loop\b/g, "`while` loop"],
    [/\bWhile\s+loop\b/g, "`while` loop"],
    [/\bwhile\s+Loop\b/g, "`while` loop"],
    [/\bWhile\s+Loop\b/g, "`while` loop"],
    [/\bmatch\s+case\b/g, "`match case`"],
    [/\bMatch\s+case\b/g, "`match case`"],
    [/\bmatch-case\b/g, "`match-case`"],
    [/\bMatch-case\b/g, "`match-case`"],
    [/\bswitch-case\b/g, "`switch-case`"],
    [/\bSwitch-case\b/g, "`switch-case`"],
    [/\bincluding if,\s*else and elif\b/g, "including `if`, `else` and `elif`"],
    [/\bIncluding if,\s*else and elif\b/g, "Including `if`, `else` and `elif`"],
    [/\bTrue\b/g, "`True`"],
    [/\bFalse\b/g, "`False`"],
    [/\bNone\b/g, "`None`"],
    [/\{\}/g, "`{}`"],
  ];

  for (const [pattern, replacement] of replacements) {
    next = next.replace(pattern, replacement);
  }

  return next;
}

function normalizeMarkdownBody(body) {
  const lines = body.split("\n");
  let inFence = false;

  const output = lines.map((line) => {
    if (/^\s*```/.test(line)) {
      inFence = !inFence;
      return line;
    }

    if (inFence) {
      return line;
    }

    // Skip raw HTML blocks and table separators.
    if (/^\s*</.test(line) || /^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$/.test(line)) {
      return line;
    }

    return replaceOutsideInlineCode(line, normalizeProseChunk);
  });

  return output.join("\n");
}

let changed = 0;
const files = TUTORIAL_DIRS.flatMap((dir) => getFilesRecursive(dir));

for (const filePath of files) {
  const original = fs.readFileSync(filePath, "utf8");
  const { frontMatter, body } = splitFrontMatter(original);
  const normalizedBody = normalizeMarkdownBody(body);
  const updated = `${frontMatter}${normalizedBody}`;

  if (updated !== original) {
    fs.writeFileSync(filePath, updated);
    changed += 1;
  }
}

console.log(`Normalized inline-code styling in ${changed} tutorial file(s).`);
