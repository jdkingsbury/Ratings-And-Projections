const insertFunctionMap = require("./functionMapping").insertFunctionMap;
const readJsonFile = require("./readJson");

const insertData = async (dataType, filePath) => {
  try {
    // NOTE: Uses the readJsonFile function to read the JSON file
    console.log("Reading data from file:", filePath);
    const data = readJsonFile(filePath);

    // NOTE: Gets the corresponding insert function from the map based on the data type
    const insertFunction = insertFunctionMap[dataType];

    if (insertFunction) {
      await insertFunction(data);
      console.log(`Data inserted successfully for ${dataType}`);
    } else {
      console.error("Unknown data type:", dataType);
    }
  } catch (err) {
    console.error(`Error inserting data for ${dataType}:`, err);
    throw err;
  }
};

module.exports = insertData;
