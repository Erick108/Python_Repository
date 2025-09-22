import psycopg2
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

password = os.getenv("SUPABASE_PASSWORD")

if password is None:
    raise ValueError("❌ La variable SUPABASE_PASSWORD no está definida en .env")

encoded_password = quote_plus(password)

host = "aws-0-us-east-2.pooler.supabase.com"
dbname = "postgres"
user = "postgres.eqhuafhkuollnehjhjoi"

DATABASE_URL = f"postgresql://{user}:{encoded_password}@{host}:5432/{dbname}"

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Conectado a Supabase desde Python")

    cur = conn.cursor()
    #cur.execute("SELECT version();")
    #version = cur.fetchone()
    #print("Versión de PostgreSQL:", version[0])

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
    """, ("Erick", "erick@example.com"))

    # Obtener el ID del registro insertado
    nuevo_id = cur.fetchone()[0]
    conn.commit()  # ¡Importante! Guarda los cambios

    print(f"✅ Usuario insertado con ID: {nuevo_id}")


    cur.close()
    conn.close()
    print("Conexión cerrada")

except Exception as e:
    print("Error:", e)    