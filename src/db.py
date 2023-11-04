import psycopg2

conn = psycopg2.connect(
    database="proyecto",
    user="sistema",
    password="admin",
    host="localhost",
    port="5432"
)