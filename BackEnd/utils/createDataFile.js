const { exec } = require("child_process");
const path = require("path");

const createDataFile = (functionName, format, args) => {
  const scriptPath = path.join(__dirname, "../services/create_file.py");
  const command = `python3 ${scriptPath} ${functionName} ${format} ${args.join(" ")}`;

  return new Promise((resolve, reject) => {
    exec(command, (error, stdout, stderr) => {
      if (error) {
        return reject(error);
      }
      if (stderr) {
        return reject(stderr);
      }
      console.log(`Stdout: ${stdout}`);
      resolve(stdout);
    });
  });
};

module.exports = createDataFile;
