import psycopg2
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os
load_dotenv()

def obtener_conexion():

    host = os.getenv("SUPABASE_HOST") #La direccion del servidor
    dbname = os.getenv("SUPABASE_DBNAME") #Nombre de la base de datos
    user = os.getenv("SUPABASE_USER") #El usuario
    password = os.getenv("SUPABASE_PASSWORD") #La contraseña que se toma del archivo .env

    if password is None:
        raise ValueError("❌ La variable SUPABASE_PASSWORD no está definida en .env")

    encoded_password = quote_plus(password)

    DATABASE_URL = f"postgresql://{user}:{encoded_password}@{host}:5432/{dbname}"

    try: 
        conn = psycopg2.connect(DATABASE_URL)
        print("Conectado a Supabase desde Python")
        return conn
        #conn.close()
        #print("Conexión cerrada")

    except Exception as e:
        print("Error:", e) 
        return None