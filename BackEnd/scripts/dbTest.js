const { Pool } = require('pg');
const dotenv = require("dotenv");

dotenv.config();

const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_DATABASE,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

// Define the SQL queries
const createTableQuery = `
  CREATE TABLE IF NOT EXISTS sample_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INT
  );
`;

const insertDataQuery = `
  INSERT INTO sample_table (name, age) VALUES ($1, $2) RETURNING *;
`;

const fetchDataQuery = `
  SELECT * FROM sample_table;
`;

const checkTableExistsQuery = `
  SELECT to_regclass('public.sample_table') AS exists;
`;

// Main function to perform database operations
const main = async () => {
  let client;

  try {
    // Connect to the database
    client = await pool.connect();
    console.log("Connected to the database");

    // Verify connection details
    console.log("Database connection details:", {
      user: process.env.DB_USER,
      host: process.env.DB_HOST,
      database: process.env.DB_DATABASE,
      port: process.env.DB_PORT,
    });

    // Check if table exists
    const checkTableExistsResult = await client.query(checkTableExistsQuery);
    console.log("Check table exists result:", checkTableExistsResult.rows);

    // Create table
    await client.query(createTableQuery);
    console.log("Table created or already exists");

    // Insert data
    const insertResult = await client.query(insertDataQuery, ['John Doe', 30]);
    console.log("Inserted data:", insertResult.rows[0]);

    // Fetch data
    const fetchResult = await client.query(fetchDataQuery);
    console.log("Fetched data:", fetchResult.rows);

  } catch (err) {
    console.error('Error executing query', err.stack);
  } finally {
    // Release the client if it was successfully acquired
    if (client) {
      client.release();
    }
    // End the pool to close all connections
    await pool.end();
    console.log("Pool ended");
  }
};

// Execute the main function
main();
