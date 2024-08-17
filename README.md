# Sports Prediction Application

## Table of Contents

- [Overview](#overview)
- [Backend](#backend)
- [Frontend](#frontend)
- [Installation](#installation)
- [Usage](#usage)
- [Creating JSON and CSV Files](#creating-json-and-csv-files)

## Overview

This project aims to provide player and team grades and future projections from data retrieved from APIs like [nba_api](https://github.com/swar/nba_api/tree/master) and web scraping tools.

## Frontend

The frontend is built using Next.js, a React-based framework for building modern web applications.

## Backend

The backend uses FastAPI and contains the API endpoints and service files. It handles:
- Fetching data from external APIs
- Processing and storing data in the PostgreSQL database
- Generating player and team grades
- Exposing endpoints for the frontend

## Database

The Application uses PostgreSQL as the database. It stores detailed information about players, teams, and game logs. The schema currently includes tables for:
- Players
- Teams
- Game Logs

## Installation

_Currently working on improving this._

### Prerequisites

- Node.js (v14 or later)
- Python (v.3.8 or later)
- npm (v6 or later)
- pip (v20 or later)
- Docker
- Docker Compose

The Application uses Docker to run the Application.

### Steps

1. **Clone the repository:**

```sh
git clone https://github.com/jdkingsbury/Sports_Prediction.git
cd Sports_Prediction
```

2. Set environment variables in both the frontend, backend, and root directories.

   - backend: Provide the DB URLs for the variables DATABASE_URL and ASYNC_DATABASE_URL.
   - frontend: Provide the URL to the backend of the Application.
   - root: Provide the database information.

     Example of .env file in the backend directory:

     ```env
     DATABASE_URL=postgresql://<username>:<password>@<host>:<port>/<dbname>
     ASYNC_DATABASE_URL=postgresql+asyncpg://<username>:<password>@<host>:<port>/<dbname>
     ```

3. **Install using Docker Compose**

```sh
docker-compose up --build
```

4. Run Python setup script

```sh
docker-compose run backend python app/scripts/populate_db.py
```

If you experience an error with shadcn when viewing a page, install shadcn.

## Usage

Docker will build and start up the frontend, backend, and the database for the Application. Access the frontend at [http://localhost:3000] and the backend API at [http://localhost:8000].

## Creating JSON and CSV Files

You can create JSON and CSV files for the NBA functions in `nba.py` which is located in the `routers` directory.

**Ensure the backend server and the PostgreSQL container are running to create files from the API routes in the application.**

### Example and Layout:

**CLI command:**

```sh
docker-compose exec backend python app/utils/create_file.py {api_url} {file_type} {file_name}
```

- `api_url`: The api endpoint from which to fetch players.
- `file_type`: The file type to create (json or csv).
- `file_name`: The desired name for the output file.

Example:
```sh
docker-compose exec backend python app/utils/create_file.py http://localhost:8000/nba/players json player_data
```

This command will create a player_data.json file containing player information.

- **Note**: JSON and CSV files are the only file types supported.
