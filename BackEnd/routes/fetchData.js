// routes/fetchData.js

const express = require("express");
const { exec } = require("child_process");
const path = require("path");
const router = express.Router();

router.get("/:season?", (req, res) => {
  const season = req.params.season || "2022-23";
  const scriptPath = path.join(__dirname, "../services/nba_requests.py");

  exec(`python3 ${scriptPath} ${season}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return res.status(500).send(error.message);
    }
    if (stderr) {
      console.error(`Stderr: ${stderr}`);
      return res.status(500).send(stderr);
    }
    const filePath = stdout.trim();
    res.sendFile(path.resolve(filePath));
  });
});

module.exports = router;
