#adaptador sw conexion a la base de datos en PostgreSQL
#encapsula la conexion para evitar dependencias en el dominio 
import os
import psycopg2
from psycopg2.extras import RealDictCursor

# Opcional: carga variables desde .env en dev
# Si instalaste python-dotenv, esta llamada leerá .env automáticamente.
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # dotenv no es crítico: en producción usualmente las vars vienen del entorno
    pass

class DatabaseConnection:
    def __init__(self):
        # lee variables de entorno con valores por defecto cuando aplique
        dbname = os.getenv("DB_NAME", "customers_db")
        user = os.getenv("DB_USER", "postgres")
        password = os.getenv("DB_PASS", "")
        host = os.getenv("DB_HOST", "localhost")
        port = os.getenv("DB_PORT", "5432")
        sslmode = os.getenv("DB_SSLMODE", None)  # opcional

        conn_args = {
            "dbname": dbname,
            "user": user,
            "password": password,
            "host": host,
            "port": port
        }

        # añade sslmode si está definido
        if sslmode:
            conn_args["sslmode"] = sslmode

        # crea la conexión
        self.connection = psycopg2.connect(**conn_args)
        self.connection.autocommit = True

    def get_cursor(self):
        return self.connection.cursor(cursor_factory=RealDictCursor)