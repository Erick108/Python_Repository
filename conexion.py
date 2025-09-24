import psycopg2 #Importa el modulo 'psycopg2' que es el adaptador de PostgreSQL para Python
from urllib.parse import quote_plus #quote_plus, que codifica caracteres especiales en URLs.
from dotenv import load_dotenv #load_dotenv, carga las variables de entrono desde un archivo .env
import os #Permite acceder a dichas variables

load_dotenv() #Lee el archivo .env

password = os.getenv("SUPABASE_PASSWORD") #La contraseña que se toma del archivo .env

if password is None:
    raise ValueError("❌ La variable SUPABASE_PASSWORD no está definida en .env")

encoded_password = quote_plus(password) #Codifica la variable para que pueda ser leida, si lleva caracteres especiales

host = os.getenv("SUPABASE_HOST") #La direccion del servidor
dbname = os.getenv("SUPABASE_DBNAME") #Nombre de la base de datos
user = os.getenv("SUPABASE_USER") #El usuario

DATABASE_URL = f"postgresql://{user}:{encoded_password}@{host}:5432/{dbname}"
#DATABASE_URL, Construye la URL de conexión completa con el formato que PostgreSQL entiende.
try: 
    conn = psycopg2.connect(DATABASE_URL)
    print("Conectado a Supabase desde Python")

    cur = conn.cursor()
    cur.execute("SELECT version();")
    version = cur.fetchone()
    print("Versión de PostgreSQL:", version[0])

#    cur.execute("""
#        CREATE TABLE IF NOT EXISTS usuarios (
#            id SERIAL PRIMARY KEY,
#            nombre VARCHAR(100) NOT NULL,
#            email VARCHAR(100) UNIQUE NOT NULL,
#            creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#            );
#        """)
    
#    conn.commit()
#    print("Tabla 'usuarios' creada o ya existía")

 # Insertar un usuario
    cur.execute("""
        INSERT INTO usuarios (nombre, email)
        VALUES (%s, %s)
        RETURNING id;
    """, ("Josué", "josue@example.com"))

    # Obtener el ID del registro insertado
    nuevo_id = cur.fetchone()[0]
    conn.commit()  # ¡Importante! Guarda los cambios

    print(f"✅ Usuario insertado con ID: {nuevo_id}")


    cur.close()
    conn.close()
    print("Conexión cerrada")

except Exception as e:
    print("Error:", e)    