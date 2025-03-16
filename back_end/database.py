import psycopg2
import os

host     = os.getenv("DATABASE_HOST", "localhost")
port     = os.getenv("DATABASE_PORT", "5432")
database = os.getenv("DATABASE_NAME", "Usuarios")
user     = os.getenv("USER", "postgres")
passwd   = os.getenv("PASS", "admin")

DATABASE_URL=f"postgresql://{user}:{passwd}@{host}:{port}/{database}"

def get_db_connection():
    """Establece y retorna una conexión a la base de datos."""
    try:
        conn = psycopg2.connect(DATABASE_URL)
        return conn
    except psycopg2.OperationalError as ex:
        print(f"Error al conectar a la base de datos: {ex}")
        return None
