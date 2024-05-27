# NBA Prediction Application

This is an NBA Prediction application, which consists of a backend built with Node.js and Python, and the frontend will be built with React.

## Table of Contents

- [Overview](#overview)
- [Backend](#backend)
- [Frontend](#frontend)
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Legacy Code](#legacy-code)

## Overview

This project aims to provide player grades and projections from data retrieved from the NBA API. Goal is to use the data to be able to train an AI on how to grade players.

## Backend

The backend consists of Node.js for handling HTTP requests and Python for interacting with the NBA API and performing data processing.

For detailed information, please refer to the [Backend README](Backend/README.md).

## Installation

### Prerequisites

- Node.js (v14 or later)
- Python (v.3.8 or later)
- npm (v6 or later)
- pip (v20 or later)

### Steps

1. **Clone the repository:**

```bash
git clone https://github.com/jdkingsbury/NBA_Prediction.git
cd NBA_Prediction
```

2. **Install Backend dependencies:**

```bash
cd BackEnd
npm install
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage

### Start the Backend Server

Navigate to the `BackEnd` directory and run:

```bash
npm start
```

The server will start on <http://localhost:4000>.

## Running Tests

### Backend Tests

Navigate to the BackEnd directory and run:

#### JavaScript Tests

```bash
npm test
```

#### Python Tests

```bash
pytest
```

## API Endpoints

### Example: Get Player Game Log

**In the browser:**

<http://localhost:4000/api/data/get_player_game_log?output_format=json&player_id=2545&season_year=2023-24>

**CLI command:**

```shell
 python3 -m services.create_file get_player_game_log json 2544 2023-24
```

- Change json to csv if you the data in csv format.

## Legacy Code

The `legacy_code` directory contains old Python scripts that were previously used for database operations, JSON file reading, and data insertion. These scripts are kept for reference and future use, but are not part of the active codebase.

### Files

- `old_db_operations.py`: Contains old database connection and operation functions.
- `old_json_reader.py`: Contains old functions for reading JSON files.
- `old_data_insertion.py`: Contains old data insertion functions.
- `old_data_retrieval.py`: Contains old data retrieval functions.
- `old_insert_data.py`: Contains old generic insertion function used in conjunction with function mappings and data insertion functions.
- `old_retrieve_data.py`: Contains old generic function used in conjunction with function mappings and data retrieval functions.
- `old_retrieve_and_calc_data`: Contains old generic function similar to retrieve_data but used functions stat calculation functions to calculate results.

These files are not used in the current implementation but may provide useful reference for future updates or migrations.
