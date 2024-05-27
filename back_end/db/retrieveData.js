const retrieveFunctionMap = require('./functionMapping').retrieveFunctionMap;

const retrieveData = async (dataType, args) => {
  const retrieveFunction = retrieveFunctionMap[dataType];

  if (retrieveFunction) {
    try {
      const data = await retrieveFunction(...args);
      console.log(`Data retrieved successfully for ${dataType}`);
      return data;
    } catch (err) {
      console.error(`Error retrieving data for ${dataType}:`, err);
      throw err;
    }
  } else {
    console.error("Unknown data type", dataType);
    throw new Error(`Unknown data type: ${dataType}`);
  }
};

module.exports = retrieveData;
