const fs = require("fs");
const path = require("path");

const readJsonFile = (filePath) => {
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

if (require.main === module) {
  if (process.argv.length < 3) {
    console.error("Please provide a file path to the JSON file as an argument");
    process.exit(1);
  }

  const filePath = process.argv[2];

  readJsonFile(filePath);
}

module.exports = readJsonFile;
