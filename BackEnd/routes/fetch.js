// routes/fetch.js

const express = require("express");
const { exec } = require("child_process");
const path = require("path");
const fs = require("fs");
const router = express.Router();

router.get("/:functionName", (req, res) => {
  const functionName = req.params.functionName;
  const query = req.query;
  const args = Object.values(query).filter(
    (arg) => arg !== query.output_format,
  );
  const format = query.output_format || "json";
  const scriptPath = path.join(__dirname, "../services/create_file.py");

  // Construct file name based on function name and arguments
  const fileName = `${functionName}_${args.join("_")}.${format}`;
  const filePath = path.join(__dirname, "../data", fileName);

  // Check if the file already exists
  if (fs.existsSync(filePath)) {
    return res.sendFile(path.resolve(filePath));
  }

  // File does not exist, generate it using the appropriate Python script
  const command = `python3 ${scriptPath} ${functionName} ${format} ${args.join(" ")}`;
  exec(
    command,
    { cwd: path.join(__dirname, "../") },
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error: ${error.message}`);
        return res.status(500).send(error.message);
      }
      if (stderr) {
        console.error(`Stderr: ${stderr}`);
        return res.status(500).send(stderr);
      }

      // Print stdout to see the output of the print statements
      console.log(`Stdout: ${stdout}`);

      res.sendFile(path.resolve(filePath));
    },
  );
});

module.exports = router;
