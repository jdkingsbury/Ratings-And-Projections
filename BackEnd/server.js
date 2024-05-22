// server.js
const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
require("dotenv").config();

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(bodyParser.json());

// Import routes
const fetchRoute = require("./routes/fetch");
// Use routes
app.use("/fetch", fetchRoute);

app.get("/", (req, res) => {
  res.send("Hello from NBA Prediction API");
});

app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
