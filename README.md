# Sports Prediction Application

## Table of Contents

- [Overview](#overview)
- [Backend](#backend)
- [Frontend](#frontend)
- [Installation](#installation)
- [Usage](#usage)
- [Creating JSON and CSV Files](#creating-json-and-csv-files)

## Overview

This project aims to provide player and team grades and their future projections from data retrieved from APIs like [nba_api](https://github.com/swar/nba_api/tree/master) and web scraping tools.

## Frontend

The frontend is built using Next.js, a React-based framework for building modern web applications.

## Backend

The backend uses FastAPI and contains the API endpoints and service files.

## Database

The Application uses PostgreSQL as the database.

## Installation

### Prerequisites

- Node.js (v14 or later)
- Python (v.3.8 or later)
- npm (v6 or later)
- pip (v20 or later)
- Docker
- Docker Compose

The application uses Docker to run the application.

### Steps

1. **Clone the repository:**

```sh
git clone https://github.com/jdkingsbury/NBA_Prediction.git
cd NBA_Prediction
```

2. **Install using Docker Compose**

```sh
docker-compose up --build
```

3. Run Python setup script

```sh
docker-compose run backend python app/scripts/populate_db.py
```

## Usage

Docker will build and start up the frontend, backend, and the database for the application.

## Creating JSON and CSV Files

_This section will be updated since the database now is running and the routes will be changed to pull from the database._

You can create JSON and CSV files for the NBA functions in `nba.py` located in the `routers` directory.

**The backend server must be running to use create_file.**

### Example and Layout:

**CLI command:**

Example:

```bash
python3 -m services.create_file nba players json 1630173 2023-24 5 player-game-log
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

- CSV and JSON files are the only supported file types.

### Notes:

- Ensure that Docker is properly set up and running on your machine before following the instructions.
