import psycopg2

# NOTE: This is a local connection to the database.
conn = psycopg2.connect(
    database="nba_data",
    host="localhost",
    user="jerrykingsbury",
    port="5432",
)

cursor = conn.cursor()
