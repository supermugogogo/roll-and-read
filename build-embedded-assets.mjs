import { readFile, writeFile } from "node:fs/promises";
import { resolve } from "node:path";

const root = process.cwd();
const appSource = await readFile(resolve(root, "app.js"), "utf8");
let detailSource = "";
try {
  detailSource = await readFile(resolve(root, "all-worksheet-details.js"), "utf8");
} catch {}
const combinedSource = `${appSource}\n${detailSource}`;
const filenames = [
  ...combinedSource.matchAll(/file: "([^"]+\.png)"/g),
  ...combinedSource.matchAll(/"file":"([^"]+\.png)"/g)
].map((match) => match[1]);
const uniqueFilenames = [...new Set(filenames)];
const assets = {};

for (const filename of uniqueFilenames) {
  try {
    const image = await readFile(resolve(root, filename));
    assets[filename] = `data:image/png;base64,${image.toString("base64")}`;
  } catch {
    // A generated detail entry may replace a legacy root-level path.
  }
}

const output = `/* Generated from the worksheet PNG files. */\n` +
  `globalThis.WORKSHEET_ASSETS = Object.freeze(${JSON.stringify(assets)});\n`;

await writeFile(resolve(root, "worksheet-assets.js"), output, "utf8");
console.log(`Embedded ${Object.keys(assets).length} worksheet files.`);
