const insertFunctionMap = require("./functionMapping");
const readJsonFile = require("./readJson");

const insertData = async (dataType, filePath) => {
  // NOTE: Uses the readJsonFile function to read the JSON file
  const data = readJsonFile(filePath);

  // NOTE: Gets the corresponding insert function from the map based on the data type
  const insertFunction = insertFunctionMap[dataType];

  console.log("Insert function:", insertFunction);
  if (insertFunction) {
    try {
      await insertFunction(data);
      console.log(`Data inserted successfully for ${dataType}`);
    } catch (err) {
      console.error("Unknown data type:", dataType);
    }
  }
};

module.exports = insertData;
