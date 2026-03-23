(() => {
  function renderMermaidBlocks() {
    const mermaidCodeBlocks = document.querySelectorAll(
      "pre code.language-mermaid",
    );
    if (!mermaidCodeBlocks.length) {
      return;
    }

    mermaidCodeBlocks.forEach((codeBlock) => {
      const pre = codeBlock.closest("pre");
      if (!pre) {
        return;
      }

      const container = document.createElement("div");
      container.className = "mermaid";
      container.textContent = codeBlock.textContent;
      pre.replaceWith(container);
    });

    window.mermaid.initialize({
      startOnLoad: false,
      theme: "neutral",
      securityLevel: "loose",
      flowchart: { useMaxWidth: true, htmlLabels: true },
    });

    window.mermaid.run({ querySelector: ".mermaid" });
  }

  function loadMermaid() {
    if (!document.querySelector("pre code.language-mermaid")) {
      return;
    }

    if (window.mermaid) {
      renderMermaidBlocks();
      return;
    }

    const existing = document.querySelector(
      "script[data-mermaid-loader='true']",
    );
    if (existing) {
      existing.addEventListener("load", renderMermaidBlocks, { once: true });
      return;
    }

    const script = document.createElement("script");
    script.src = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js";
    script.defer = true;
    script.dataset.mermaidLoader = "true";
    script.onload = renderMermaidBlocks;
    script.onerror = () => {
      console.error("Failed to load Mermaid.");
    };

    document.head.appendChild(script);
  }

  document.addEventListener("DOMContentLoaded", loadMermaid);
})();
