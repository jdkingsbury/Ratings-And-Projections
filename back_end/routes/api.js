// routes/api.js

const express = require("express");
const path = require("path");
const fs = require("fs");
const router = express.Router();
const checkDatabase = require("../utils/checkDataBase");
const checkFileSystem = require("../utils/checkFileSystem");
const createDataFile = require("../utils/createDataFile");
const insertData = require("../db/insertData");

router.get("/data/:functionName", async (req, res) => {
  const functionName = req.params.functionName;
  const query = req.query;
  const format = query.output_format || "json";
  const args = Object.values(query).filter((arg) => arg !== query.output_format);

  let cleanFunctionName = functionName;
  if (cleanFunctionName.startsWith("get_")) {
    cleanFunctionName = cleanFunctionName.slice(4);
  }

  // Construct file name based on function name and arguments
  const fileName = `${cleanFunctionName}_${args.join("_")}.${format}`;
  const filePath = path.join(__dirname, "../data", fileName);

  console.log(`Function Name: ${cleanFunctionName}`);
  console.log(`Arguments: ${args}`);
  console.log(`Output Format: ${format}`);
  console.log(`Constructed file name: ${fileName}`);
  console.log(`Checking database for existing data...`);

  try {
    // Check the database for existing data
    const dbData = await checkDatabase(cleanFunctionName, args);
    if (dbData) {
      console.log(`Data found in database for ${cleanFunctionName}`);
      if (format === "csv") {
        // Covert to CSV if needed
        const csvFilePath = path.join(
          __dirname,
          "../data",
          `${cleanFunctionName}_${args.join("_")}.csv`,
        );
        console.log(`Sending CSV file: ${csvFilePath}`);
        return res.sendFile(path.resolve(csvFilePath));
      }
      // Convert to JSON if needed
      console.log(`Sending JSON data from database`)
      return res.json(dbData);
    }

    console.log(`Data not found in database for ${cleanFunctionName}`);
    console.log(`Checking file system for existing data...`);
    // Check if the file already exists
    const fileData = checkFileSystem(filePath);
    if (fileData) {
      console.log(`File exists. Sending file: ${filePath}`);
      return res.sendFile(path.resolve(filePath));
    }

    console.log(`File does not exist. Generating file using the appropriate Python script...`);
    // File does not exist, generate it using the appropriate Python script
    await createDataFile(cleanFunctionName, format, args);

    // Read newly created file
    const dataFile = fs.readFileSync(filePath, "utf-8");

    // Insert data into the database if in JSON format
    if (format === "json") {
      const data = JSON.parse(dataFile);
      console.log(`Inserting data into database for ${cleanFunctionName}`);
      await insertData(cleanFunctionName, filePath);
      console.log(`Sending JSON data from newly created file`);
      return res.json(data);
    }

    // Return the file to the client
    res.sendFile(path.resolve(filePath));
  } catch (err) {
    console.log("Error:", err);
    res.status(500).send(err.message);
  }
});

module.exports = router;
