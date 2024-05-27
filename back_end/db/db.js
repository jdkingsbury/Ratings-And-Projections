const { Pool } = require('pg');
const dotenv = require('dotenv');

dotenv.config();

const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST,
  database: process.env.DB_DATABASE,
  password: process.env.DB_PASSWORD,
  port: process.env.DB_PORT,
});

pool.on('connect', () => {
 console.log('Connected to PostgreSQL');
});

pool.on('error', (err) => {
  console.error('Connection error', err.stack);
});

module.exports = pool;
