import psycopg2
from .config import DATABASE_CONFIG


# NOTE: This function connects to the database and returns the connection object.
def connect_to_database():
    try:
        conn = psycopg2.connect(**DATABASE_CONFIG)
        return conn
    except psycopg2.Error as e:
        print(f"Error: Could not connect to the database. {e}")
        return None
