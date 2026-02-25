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

function checkTutorialMetadata(errors) {
  const tutorialDir = path.join(process.cwd(), "tutorial");
  const tutorialFiles = getFilesRecursive(tutorialDir, (filePath) => filePath.endsWith(".md")).sort();

  if (tutorialFiles.length === 0) {
    errors.push("No tutorial markdown files were found.");
    return { permalinks: new Set(["/"]) };
  }

  const orders = [];
  const permalinks = new Set(["/"]);

  for (const filePath of tutorialFiles) {
    const relativePath = path.relative(tutorialDir, filePath).replace(/\\/g, "/");
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

    if (!frontMatter.permalink.startsWith("/tutorial/")) {
      errors.push(`${relativePath} permalink should start with /tutorial/.`);
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
    errors.push("Duplicate tutorial order values detected.");
  }

  for (let expected = 1; expected <= tutorialFiles.length; expected += 1) {
    if (!orderSet.has(expected)) {
      errors.push(`Tutorial order ${expected} is missing.`);
    }
  }

  return { permalinks };
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
  ];

  const hrefRegex = /href=["'](\/[^"'#?\s]+)\/?["']/g;

  for (const file of sourceFiles) {
    const content = fs.readFileSync(file, "utf8");
    let match = hrefRegex.exec(content);
    while (match) {
      const href = match[1].replace(/\/$/, "") || "/";
      if (!href.startsWith("/img/") && !href.startsWith("/css/") && !permalinks.has(href)) {
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
const { permalinks } = checkTutorialMetadata(errors);
checkPermalinksAndLinks(permalinks, errors);
checkLegacyMarkers(errors);

if (errors.length > 0) {
  fail(errors);
}

console.log("Content checks passed.");
