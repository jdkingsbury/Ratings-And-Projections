const fs = require('fs')

const checkFileSystem = (filePath) => {
  if (fs.existsSync(filePath)) {
    const jsonData = fs.readFileSync(filePath, "utf-8");
    return JSON.parse(jsonData);
  }
  return null;
};

module.exports = checkFileSystem;
