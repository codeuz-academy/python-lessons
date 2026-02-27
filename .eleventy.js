const markdownIt = require("markdown-it");
const fs = require("fs");
const nodePath = require("path");

function normalizePathPrefix(rawPathPrefix = "/") {
  if (!rawPathPrefix || rawPathPrefix === "/") {
    return "/";
  }
  return `/${rawPathPrefix.replace(/^\/+|\/+$/g, "")}/`;
}

module.exports = function (eleventyConfig) {
  const pathPrefix = normalizePathPrefix(process.env.ELEVENTY_PATH_PREFIX);
  const pathPrefixWithoutTrailingSlash = pathPrefix === "/"
    ? "/"
    : pathPrefix.slice(0, -1);
  const pathPrefixKey = pathPrefix.replace(/^\/|\/$/g, "");

  const md = markdownIt({
    html: true,
    breaks: false,
    linkify: true
  });

  eleventyConfig.setLibrary("md", md);

  eleventyConfig.addPassthroughCopy({ "assets/img": "img" });
  eleventyConfig.addPassthroughCopy({ "assets/css": "css" });
  eleventyConfig.addPassthroughCopy({ "assets/js": "js" });
  eleventyConfig.addPassthroughCopy(".nojekyll");
  eleventyConfig.addPassthroughCopy({ "assets/img/favicon.png": "favicon.png" });

  eleventyConfig.addFilter("htmlDateString", (dateObj) => {
    return new Date(dateObj).toISOString().split('T')[0];
  });

  eleventyConfig.addFilter("fileLastModified", function (inputPath, langCode) {
    if (!inputPath) {
      return null;
    }

    try {
      const normalizedPath = String(inputPath).replace(/^\.\/+/, "");
      const absolutePath = nodePath.resolve(process.cwd(), normalizedPath);
      const stats = fs.statSync(absolutePath);
      const locale = langCode === "uz" ? "uz-UZ" : "en-US";
      return new Intl.DateTimeFormat(locale, {
        year: "numeric",
        month: "long",
        day: "numeric"
      }).format(stats.mtime);
    } catch (_error) {
      return null;
    }
  });

  eleventyConfig.addFilter("urlencode", function (str) {
    return encodeURIComponent(str);
  });

  eleventyConfig.addFilter("padStart", function (value, length, char) {
    return String(value).padStart(length || 2, char || "0");
  });

  eleventyConfig.addFilter("displayTutorialTitle", function (value) {
    if (typeof value !== "string") {
      return value;
    }

    const original = value.trim();
    if (!original) {
      return value;
    }

    let title = original.replace(/\s+/g, " ");
    const titleBeforeLeadingStrip = title;

    // Remove common tutorial title wrappers that redundantly include "Python".
    title = title.replace(/\s*\(\s*Python\s*\)\s*$/i, "");
    title = title.replace(/\s+(?:to|in|with|for|on)\s+Python$/i, "");
    title = title.replace(/\s+Python$/i, "");
    title = title.replace(/^Python'(?:ga|ni|da|ning)\s+/i, "");
    title = title.replace(/^Python(?:ga|ni|da|ning)\s+/i, "");
    title = title.replace(/^Python\s+/i, "");

    title = title.trim();
    if (titleBeforeLeadingStrip !== title && /^[a-z]/.test(title)) {
      title = title.charAt(0).toUpperCase() + title.slice(1);
    }

    return title || original;
  });

  eleventyConfig.addFilter("getTutorialNav", function (tutorials, currentUrl) {
    if (!Array.isArray(tutorials) || !currentUrl) {
      return { first: null, prev: null, next: null };
    }

    const currentIndex = tutorials.findIndex((item) => item.url === currentUrl);
    const first = tutorials.length > 0 ? tutorials[0] : null;
    const prev = currentIndex > 0 ? tutorials[currentIndex - 1] : null;
    const next = currentIndex >= 0 && currentIndex < tutorials.length - 1
      ? tutorials[currentIndex + 1]
      : null;

    return { first, prev, next };
  });

  eleventyConfig.addCollection("tutorials", function (collectionApi) {
    return collectionApi.getFilteredByGlob("content/en/tutorial/**/*.md").sort((a, b) => {
      return (a.data.order || 0) - (b.data.order || 0);
    });
  });

  eleventyConfig.addCollection("tutorialsUz", function (collectionApi) {
    return collectionApi.getFilteredByGlob("content/uz/tutorial/**/*.md").sort((a, b) => {
      return (a.data.order || 0) - (b.data.order || 0);
    });
  });

  eleventyConfig.addCollection("tools", function (collectionApi) {
    return collectionApi.getFilteredByGlob("tools/*.njk");
  });

  eleventyConfig.addWatchTarget("./assets/css/");
  eleventyConfig.addWatchTarget("./assets/js/");
  eleventyConfig.addWatchTarget("./tailwind.css");

  eleventyConfig.setServerOptions({
    watch: ["_site/css/**/*.css"],
    liveReload: true,
  });

  eleventyConfig.addTransform("prefixRootRelativeUrls", function (content, outputPath) {
    const currentOutputPath = outputPath || this?.page?.outputPath || this?.outputPath;

    if (!currentOutputPath || !currentOutputPath.endsWith(".html") || pathPrefix === "/") {
      return content;
    }

    return content.replace(/\b(href|src|poster)=("|')\/(?!\/)([^"']*)\2/g, (match, attr, quote, targetPath) => {
      if (targetPath === pathPrefixKey || targetPath.startsWith(`${pathPrefixKey}/`)) {
        return match;
      }
      return `${attr}=${quote}${pathPrefixWithoutTrailingSlash}/${targetPath}${quote}`;
    });
  });

  return {
    pathPrefix,
    dir: {
      input: ".",
      output: "_site",
      includes: "_includes",
      layouts: "_layouts",
      data: "_data"
    },
    templateFormats: ["md", "njk", "html"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
    passthroughFileCopy: true
  };
};
