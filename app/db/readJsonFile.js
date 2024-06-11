import fs from "fs";
import path from "path";

export default function readJsonFile(filePath) {
  try {
    // Read and parse the JSON file
    const absolutePath = path.resolve(filePath);
    const fileContent = fs.readFileSync(absolutePath, "utf-8");
    const data = JSON.parse(fileContent);
    return data;
  } catch (err) {
    console.error("Error reading or parsing the file: ", err);
    throw err;
  }
};
