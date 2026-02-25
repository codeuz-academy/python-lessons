const markdownIt = require("markdown-it");

module.exports = function (eleventyConfig) {
  const md = markdownIt({
    html: true,
    breaks: false,
    linkify: true
  });

  eleventyConfig.setLibrary("md", md);

  eleventyConfig.addPassthroughCopy({ "assets/img": "img" });
  eleventyConfig.addPassthroughCopy({ "assets/css": "css" });
  eleventyConfig.addPassthroughCopy("CNAME");
  eleventyConfig.addPassthroughCopy(".nojekyll");
  eleventyConfig.addPassthroughCopy({ "assets/img/favicon.png": "favicon.png" });

  eleventyConfig.addFilter("htmlDateString", (dateObj) => {
    return new Date(dateObj).toISOString().split('T')[0];
  });

  eleventyConfig.addFilter("urlencode", function (str) {
    return encodeURIComponent(str);
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
    return collectionApi.getFilteredByGlob("tutorial/**/*.md").sort((a, b) => {
      return (a.data.order || 0) - (b.data.order || 0);
    });
  });

  eleventyConfig.addCollection("tools", function (collectionApi) {
    return collectionApi.getFilteredByGlob("tools/*.njk");
  });

  eleventyConfig.addWatchTarget("./assets/css/");
  eleventyConfig.addWatchTarget("./tailwind.css");

  eleventyConfig.setServerOptions({
    watch: ["_site/css/**/*.css"],
    liveReload: true,
  });

  return {
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
