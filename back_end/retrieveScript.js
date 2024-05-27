const retrieveData = require(`./db/retrieveData`);
const pool = require(`./db/db`);

const main = async () => {
  const args = process.argv.slice(2);

  if (args.length < 2) {
    console.error("Usage: node retrieveScript.js <dataType> <arg1> <arg2> ...");
    process.exit(1);
  }

  const dataType = args[0];
  const functionArgs = args.slice(1);

  try {
    const data = await retrieveData(dataType, functionArgs);
    console.log("Retrieved data:", JSON.stringify(data, null, 2));
  } catch (err) {
    console.error("Error retrieving data:", err);
  } finally {
    pool.end(); // Close connection pool
  }
};

main();
