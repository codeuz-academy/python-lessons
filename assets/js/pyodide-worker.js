self.__PYODIDE_CDN__ = "https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js";

let pyodideReadyPromise = null;

async function getPyodideInstance() {
  if (!pyodideReadyPromise) {
    self.importScripts(self.__PYODIDE_CDN__);
    pyodideReadyPromise = self.loadPyodide();
  }
  return pyodideReadyPromise;
}

function toMessageError(err) {
  if (!err) {
    return "Unknown error";
  }
  if (typeof err === "string") {
    return err;
  }
  return err.message || String(err);
}

self.onmessage = async (event) => {
  const payload = event.data || {};
  const { type, id } = payload;

  if (type === "preload") {
    try {
      await getPyodideInstance();
      self.postMessage({ type: "preload:ok", id });
    } catch (err) {
      self.postMessage({ type: "preload:error", id, error: toMessageError(err) });
    }
    return;
  }

  if (type !== "run") {
    return;
  }

  const stdoutBuffer = [];
  const stderrBuffer = [];
  const globalsToDelete = [];

  try {
    const py = await getPyodideInstance();

    py.setStdout({
      batched: (str) => {
        stdoutBuffer.push(str);
      }
    });

    py.setStderr({
      batched: (str) => {
        stderrBuffer.push(str);
      }
    });

    if (payload.globals && typeof payload.globals === "object") {
      for (const [key, value] of Object.entries(payload.globals)) {
        py.globals.set(key, value);
        globalsToDelete.push(key);
      }
    }

    await py.runPythonAsync(payload.code || "");

    self.postMessage({
      type: "result",
      id,
      stdout: stdoutBuffer.join("\n"),
      stderr: stderrBuffer.join("\n")
    });
  } catch (err) {
    self.postMessage({
      type: "error",
      id,
      error: toMessageError(err),
      stdout: stdoutBuffer.join("\n"),
      stderr: stderrBuffer.join("\n")
    });
  } finally {
    if (globalsToDelete.length) {
      try {
        const py = await getPyodideInstance();
        for (const key of globalsToDelete) {
          try {
            py.globals.delete(key);
          } catch (_err) {
            // Ignore cleanup failures for compatibility with different Pyodide proxy behaviors.
          }
        }
      } catch (_err) {
        // Ignore cleanup failure.
      }
    }
  }
};
