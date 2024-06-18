import fs from "fs/promises";

// NOTE: Reads and parses the JSON file using the asynchronous readFile function
export async function readJsonFile(filePath) {
  try {
    const data = await fs.readFile(filePath, "utf-8");
    return JSON.parse(data);
  } catch (err) {
    console.error(`Error reading or parsing the file: ${filePath}`, err);
    throw err;
  }
}
