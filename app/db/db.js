import pg from "pg";
import dotenv from "dotenv";
import { readJsonFile } from "./readJsonFile.js";

dotenv.config();

const { Pool } = pg;

const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_DATABASE,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

pool.on("connect", () => {
  console.log("Connected to PostgreSQL");
});

pool.on("error", (err) => {
  console.error("Connection error", err.stack);
});

export default pool;
export async function queryDatabase(query, params) {
  const client = await pool.connect();
  try {
    const res = await client.query(query, params);
    return res.rows;
  } catch (err) {
    console.error("Failed to query the database:", err);
    throw err;
  } finally {
    client.release();
  }
}

export async function insertDatabase(query, filePath) {
  const client = await pool.connect();
  try {
    const data = await readJsonFile(filePath);
    const values = Object.values(data);
    await client.query(query, values);
  } catch (err) {
    console.error("Failed to insert data into the database:", err);
    throw err;
  } finally {
    client.release();
  }
}
