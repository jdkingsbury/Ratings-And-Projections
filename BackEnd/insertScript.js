const insertData = require("./db/insertData");
const path = require("path");
const fs = require("fs");
const pool = require("./db/db");

// NOTE: Function to parse the file name and return the data type
const parseFileName = (fileName) => {
  const regex = /([a-zA-Z_]+)_(\d+)_(\d{4}-\d{2})\.json/;
  const match = fileName.match(regex);
  if (match) {
    const functionIdentifier = match[1];
    const playerId = match[2];
    const seasonYear = match[3];
    return { functionIdentifier, playerId, seasonYear };
  }
  return null;
};

// NOTE: Directory containing JSON files
const dataDir = "./data";

// Function to insert data from JSON files
const insertDataFromFile = async (file) => {
  const filePath = path.join(dataDir, file);
  console.log(`Constructed file path: ${filePath}`);
  const fileInfo = parseFileName(file);

  if (fileInfo) {
    const { functionIdentifier } = fileInfo;
    console.log(`Inserting data from file: ${file}`);
    await insertData(functionIdentifier, filePath);
  } else {
  console.warn(`Skipping file: ${file} (invalid file name format)`);
    }
};

const insertAllData = async () => {
  try {
    const files = fs.readdirSync(dataDir);
    for (const file of files) {
      await insertDataFromFile(file);
    }
  } catch (err) {
    console.error("Error inserting data", err);
  } finally {
    pool.end(); // Close the database connection
  }
};

const main = async () => {
  const args = process.argv.slice(2);

  if (args.length === 0) {
    await insertAllData();
  } else {
    for (const arg of args) {
      await insertDataFromFile(arg);
    }
  }
};

main();
