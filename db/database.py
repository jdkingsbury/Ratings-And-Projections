import psycopg2

conn = psycopg2.connect(
        database="nba_data",
        host="localhost",
        user="jerrykingsbury",
        port="5432",
)

cursor = conn.cursor()
