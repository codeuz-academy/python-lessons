const fs = require("fs");
const path = require("path");

function fail(errors) {
  console.error("Content checks failed:");
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

function getFilesRecursive(dir, predicate = () => true, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      if (entry.name === "node_modules" || entry.name === ".git" || entry.name === "_site") {
        continue;
      }
      getFilesRecursive(fullPath, predicate, out);
    } else if (entry.isFile() && predicate(fullPath)) {
      out.push(fullPath);
    }
  }
  return out;
}

function parseFrontMatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---/);
  if (!match) {
    return null;
  }

  const frontMatter = match[1];
  const getValue = (key) => {
    const keyMatch = frontMatter.match(new RegExp(`^${key}:\\s*(.+)$`, "m"));
    return keyMatch ? keyMatch[1].trim() : "";
  };

  return {
    layout: getValue("layout"),
    order: Number(getValue("order")),
    permalink: getValue("permalink"),
  };
}

function checkTutorialMetadataForLocale(config, errors) {
  const tutorialFiles = getFilesRecursive(config.dir, (filePath) => filePath.endsWith(".md")).sort();
  const orders = [];
  const permalinks = new Set();
  const relativePaths = new Set();

  if (tutorialFiles.length === 0) {
    errors.push(`No tutorial markdown files were found for ${config.label}.`);
    return { permalinks, relativePaths };
  }

  for (const filePath of tutorialFiles) {
    const relativePath = path.relative(process.cwd(), filePath).replace(/\\/g, "/");
    const localeRelativePath = path.relative(config.dir, filePath).replace(/\\/g, "/");
    relativePaths.add(localeRelativePath);
    const fileName = path.basename(filePath);
    const content = fs.readFileSync(filePath, "utf8");
    const frontMatter = parseFrontMatter(content);

    if (!frontMatter) {
      errors.push(`${relativePath} is missing front matter.`);
      continue;
    }

    if (frontMatter.layout !== "tutorial.njk") {
      errors.push(`${relativePath} should use layout: tutorial.njk.`);
    }

    if (!frontMatter.permalink.startsWith(config.permalinkPrefix)) {
      errors.push(`${relativePath} permalink should start with ${config.permalinkPrefix}.`);
    } else {
      permalinks.add(frontMatter.permalink.replace(/\/$/, "") || "/");
    }

    if (Number.isNaN(frontMatter.order)) {
      errors.push(`${relativePath} has an invalid order value.`);
      continue;
    }

    orders.push(frontMatter.order);

    const prefixMatch = fileName.match(/^(\d+)-/);
    if (!prefixMatch) {
      errors.push(`${relativePath} should start with a numeric prefix (e.g. 01-...).`);
      continue;
    }

    const prefix = Number(prefixMatch[1]);
    if (prefix !== frontMatter.order) {
      errors.push(`${relativePath} order (${frontMatter.order}) should match file prefix (${prefix}).`);
    }

    if (content.includes("Edit this tutorial")) {
      errors.push(`${relativePath} still contains a hardcoded "Edit this tutorial" section.`);
    }

    if (content.includes("blob/master/docs") || content.includes("blob/master/src")) {
      errors.push(`${relativePath} contains a legacy blob/master docs/src link.`);
    }
  }

  const orderSet = new Set(orders);
  if (orderSet.size !== orders.length) {
    errors.push(`Duplicate tutorial order values detected for ${config.label}.`);
  }

  for (let expected = 1; expected <= tutorialFiles.length; expected += 1) {
    if (!orderSet.has(expected)) {
      errors.push(`${config.label} tutorial order ${expected} is missing.`);
    }
  }

  return { permalinks, relativePaths };
}

function checkLocaleParity(enPaths, uzPaths, errors) {
  for (const tutorialPath of enPaths) {
    if (!uzPaths.has(tutorialPath)) {
      errors.push(`Missing Uzbek translation file for ${tutorialPath}.`);
    }
  }

  for (const tutorialPath of uzPaths) {
    if (!enPaths.has(tutorialPath)) {
      errors.push(`Missing English tutorial file for ${tutorialPath}.`);
    }
  }
}

function checkPermalinksAndLinks(permalinks, errors) {
  const toolFiles = getFilesRecursive(path.join(process.cwd(), "tools"), (p) => p.endsWith(".njk"));
  for (const file of toolFiles) {
    const content = fs.readFileSync(file, "utf8");
    const frontMatter = parseFrontMatter(content);
    if (!frontMatter || !frontMatter.permalink) {
      continue;
    }
    permalinks.add(frontMatter.permalink.replace(/\/$/, "") || "/");
  }
  permalinks.add("/sitemap.xml");

  const sourceFiles = [
    ...getFilesRecursive(path.join(process.cwd(), "tutorial"), (p) => p.endsWith(".md")),
    ...getFilesRecursive(path.join(process.cwd(), "_includes"), (p) => p.endsWith(".njk")),
    ...getFilesRecursive(path.join(process.cwd(), "_layouts"), (p) => p.endsWith(".njk")),
    path.join(process.cwd(), "index.md"),
    path.join(process.cwd(), "uz", "index.md"),
  ];

  const hrefRegex = /href=["'](\/[^"'#?\s]+)\/?["']/g;

  for (const file of sourceFiles) {
    if (!fs.existsSync(file)) {
      continue;
    }

    const content = fs.readFileSync(file, "utf8");
    let match = hrefRegex.exec(content);
    while (match) {
      const href = match[1].replace(/\/$/, "") || "/";
      if (
        !href.startsWith("/img/") &&
        !href.startsWith("/css/") &&
        !href.startsWith("/js/") &&
        href !== "/favicon.png" &&
        !permalinks.has(href)
      ) {
        errors.push(`${path.relative(process.cwd(), file)} has broken internal href: ${href}`);
      }
      match = hrefRegex.exec(content);
    }
  }
}

function checkLegacyMarkers(errors) {
  const filesToScan = getFilesRecursive(process.cwd(), (filePath) => {
    return (
      filePath.endsWith(".md") ||
      filePath.endsWith(".njk") ||
      filePath.endsWith(".js") ||
      filePath.endsWith(".json")
    );
  });

  const forbiddenMarkers = [
    "/tutorial/decorator-python",
    "/uz/tutorial/",
    "blob/master/docs/tutorial",
    "blob/master/src/tutorial",
  ];

  for (const file of filesToScan) {
    const content = fs.readFileSync(file, "utf8");
    for (const marker of forbiddenMarkers) {
      if (content.includes(marker)) {
        errors.push(`${path.relative(process.cwd(), file)} contains forbidden marker: ${marker}`);
      }
    }
  }
}

const errors = [];
const localeConfigs = [
  {
    label: "English",
    dir: path.join(process.cwd(), "tutorial", "en"),
    permalinkPrefix: "/tutorial/en/",
  },
  {
    label: "Uzbek",
    dir: path.join(process.cwd(), "tutorial", "uz"),
    permalinkPrefix: "/tutorial/uz/",
  },
];

const localeResults = localeConfigs.map((config) => checkTutorialMetadataForLocale(config, errors));
checkLocaleParity(localeResults[0].relativePaths, localeResults[1].relativePaths, errors);

const permalinks = new Set(["/", "/uz/"]);
for (const result of localeResults) {
  for (const permalink of result.permalinks) {
    permalinks.add(permalink);
  }
}

checkPermalinksAndLinks(permalinks, errors);
checkLegacyMarkers(errors);

if (errors.length > 0) {
  fail(errors);
}

console.log("Content checks passed.");
