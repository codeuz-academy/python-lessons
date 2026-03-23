const fs = require("fs");
const path = require("path");

const siteDir = path.join(process.cwd(), "_site");
if (!fs.existsSync(siteDir)) {
  console.error("JSON-LD check failed: _site directory does not exist. Run `npm run build` first.");
  process.exit(1);
}

function getHtmlFiles(dir, out = []) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      getHtmlFiles(fullPath, out);
    } else if (entry.isFile() && fullPath.endsWith(".html")) {
      out.push(fullPath);
    }
  }
  return out;
}

const htmlFiles = getHtmlFiles(siteDir);
const errors = [];
const jsonLdRegex = /<script type="application\/ld\+json">([\s\S]*?)<\/script>/g;

for (const file of htmlFiles) {
  const content = fs.readFileSync(file, "utf8");
  let match = jsonLdRegex.exec(content);
  while (match) {
    const payload = match[1].trim();
    try {
      JSON.parse(payload);
    } catch (error) {
      errors.push(`${path.relative(process.cwd(), file)} has invalid JSON-LD: ${error.message}`);
    }
    match = jsonLdRegex.exec(content);
  }
}

if (errors.length > 0) {
  console.error("JSON-LD checks failed:");
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log("JSON-LD checks passed.");
