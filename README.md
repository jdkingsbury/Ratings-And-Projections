# Sports Prediction Application

## Table of Contents

- [Overview](#overview)
- [Backend](#backend)
- [Frontend](#frontend)
- [Installation](#installation)
- [Usage](#usage)
- [Creating JSON and CSV Files](#creating-json-and-csv-files)
- [Known Issues](#known-issues)

## Overview

This project aims to provide player and team grades and their future projections from data retrieved from [nba_api](https://github.com/swar/nba_api/tree/master).

## Frontend

The frontend is built using Next.js, a React-based framework for building modern web applications.

## Backend

The backend uses FastAPI and contains the API endpoints and service files.

## Database

The Application uses Postgres as the Database

## Installation

### Prerequisites

- Node.js (v14 or later)
- Python (v.3.8 or later)
- npm (v6 or later)
- pip (v20 or later)

### Steps

1. **Clone the repository:**

```sh
git clone https://github.com/jdkingsbury/NBA_Prediction.git
cd NBA_Prediction
```

2. **Install backend dependencies:**

```sh
python -m venv venv
source venv/bin/activate
cd backend
pip install -r requirements.txt
```

3. **Install frontend dependencies:**

```bash
cd frontend
npm install
```

## Usage

You need to start both the frontend and backend servers to run the application.

### Start the Backend Server

The backend uses FastAPI to handle API requests from the frontend.

Navigate to the `api` directory in the `backend` directory

To run in a development mode:

```bash
fastapi dev main.py
```

To run in production mode:

```bash
fastapi run main.py
```

### Start the Frontend Server

The frontend is built using Remix

Navigate to the `frontend` directory.

To run in development mode:

```bash
npm run dev
```

To run in production mode:

```bash
npm start
```

## Creating JSON and CSV Files

You can create JSON and CSV files for the NBA functions in `nba.py` located in the `routers` directory.

### Example: Get Player Game Log

**CLI command:**

Example:

```bash
python3 -m services.new_create_file nba players json 1630173 2023-24 5 player-game-log
```

Layout for creating player-game-log:

```bash
python3 -m services.create_file {sports league} {type of data} {file type} {person ID} {Season Year} {Games} {function_name}
```

Layout for creating career stats:

```bash
python3 -m services.create_file {sports league} {type of data} {file type} {person ID} {function_name}
```

Player Info:

```bash
python3 -m services.create_file {sports league} {type of data} {file type} {person ID} {function_name}
```

- If you want the file saved as a CSV change json to csv.
