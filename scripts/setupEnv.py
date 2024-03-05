import sys
sys.path.append('../')

import subprocess
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
from db.main import main as create_tables

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        print("Dependencies installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install dependencies: {e}")
        sys.exit(1)
    

def check_postgresql():
    try:
        subprocess.check_call(['psql', '--version'])
        print("PostgreSQL is installed")
    except subprocess.CalledProcessError:
        print(f"PostgreSQL is not installed or not added to Path.")
        sys.exit(1)


def create_database(dbname, user, password, host):
    try:
        connection = psycopg2.connect(dbname='postgres', user=user, password=password, host=host)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE {dbname}")
        cursor.close()
        connection.close()
        print(f"Database {dbname} created successfully")
    except psycopg2.Error as e:
        print(f"Failed to create database: {e}")
        sys.exit(1)

def setup_environment():
    create_tables()

def main():
    check_postgresql()
    install_dependencies()
    create_database('nba_data', 'postgres', '', 'localhost')
    setup_environment()

if __name__ == "__main__":
    main()
