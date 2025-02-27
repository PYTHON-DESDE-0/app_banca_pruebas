import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL", "dbname=postgres user=postgres password=root2025 host=localhost port=5432")

def get_db_connection():
    """Establece y retorna una conexión a la base de datos."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except psycopg2.OperationalError as ex:
        print(f"Error al conectar a la base de datos: {ex}")
        return None
