import sys

sys.path.append("../")

import subprocess
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from db.insert_data import main as create_tables


# NOTE: This function installs the dependencies from requirements.txt
def install_dependencies():
    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", "requirements.txt"]
        )
        print("Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)


# NOTE: This function checks if PostgreSQL is installed and added to Path
def check_postgresql():
    try:
        subprocess.check_call(["psql", "--version"])
        print("PostgreSQL is installed")
    except subprocess.CalledProcessError:
        print(
            "PostgreSQL is not installed or not added to Path. Please install PostgreSQL."
        )
        sys.exit(1)


# NOTE: This function creates a database
def create_database(dbname, user, password, host):
    connection = None
    try:
        conn_str = f"dbname=postgres user={user} host={host}"
        if password:
            conn_str += f" password={password}"
        connection = psycopg2.connect(conn_str)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {dbname}")
        cursor.close()
        connection.close()
        print(f"Database {dbname} created successfully")
    except psycopg2.OperationalError as e:
        print(f"OperationalError: {e}")
        print(
            "Attempting to connect with default settings may have failed due to missing password."
        )
        print(
            "Consider setting a password for the 'postgres' user or adjusting pg_hba.conf for trust authentication."
        )
        sys.exit(1)
    except psycopg2.Error as e:
        print(f"Failed to create database: {e}")
        sys.exit(1)
    finally:
        if connection is not None:
            connection.close()


# NOTE: This function sets up the environment
def setup_environment():
    create_tables()


# NOTE: This function is the entry point of the script
def main():
    check_postgresql()
    install_dependencies()
    create_database("nba_data", "postgres", "", "localhost")
    setup_environment()


if __name__ == "__main__":
    main()
