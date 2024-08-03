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
git clone https://github.com/jdkingsbury/Sports_Prediction.git
cd Sports_Prediction
```

2. Set environment variables in both the frontend, backend, and root directoies.

   - backend: Provide the DB URLs for the variables DATABASE_URL and ASYNC_DATABASE_URL.
   - frontend: Provide the URL to the backend of the application.
   - root: Provide the database information.

3. **Install using Docker Compose**

```sh
docker-compose up --build
```

4. Run Python setup script

```sh
docker-compose run backend python app/scripts/populate_db.py
```

If you experience and error with shadcn when viewing a page, install shadcn.

## Usage

Docker will build and start up the frontend, backend, and the database for the application.

## Creating JSON and CSV Files

You can create JSON and CSV files for the NBA functions in `nba.py` located in the `routers` directory.

**Ensure the backend server and the postgres container are running to create files from the api routes in the application.**

### Example and Layout:

**CLI command:**

Example using docker-compose

```sh
docker-compose exec backend python app/services/create_file.py {api_url} {file_type} {file_name}
```

- Note:

* JSON and CSV files are the only file types supported
