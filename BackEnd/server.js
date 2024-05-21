const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000;

app.use(cors());
app.use(bodyParser.json());

// NOTE: Endpoint to test the server
app.get('/', (req, res) => {
    res.send('Hello from NBA Prediction API');
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});
