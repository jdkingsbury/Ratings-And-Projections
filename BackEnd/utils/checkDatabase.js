const retrieveData = require("../db/retrieveData");

const checkDatabase = async (functionName, args) => {
  try {
    const data = await retrieveData(functionName, args);
    return data.length > 0 ? data : null;
  } catch (error) {
    if (error.code === '42P01') { // Postgres error code for table does not exist
      console.error(`Table for ${functionName} does not exist`);
      return null;
    }
    console.error("Error checking database:", error.message);
    throw error;
  }
};

module.exports = checkDatabase;
