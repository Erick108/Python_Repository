from conexion2 import obtener_conexion
conn = obtener_conexion()
cur = conn.cursor()

def crear_tabla():
    if conn is None:
        print("No se pudo conectar a la base de datos")
        return
    
    try:
        cur.execute(f"""
        CREATE TABLE IF NOT EXISTS usuarios (
           id SERIAL PRIMARY KEY,
           nombre VARCHAR(100) NOT NULL,
           email VARCHAR(100) UNIQUE NOT NULL,
           creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
           );
    """)
    
        conn.commit()
        print("Tabla 'usuarios' creada o ya existía")
    except Exception as e:
        print("Error al crear tabla:", e)
        conn.rollback()


def insertar_dato(nombre, email):
    
    if conn is None:
        print("No se pudo conectar a la base de datos")
        return
    
    try:
        cur.execute("""
            INSERT INTO usuarios (nombre, email)
            VALUES (%s, %s)
                RETURNING id;
        """, (nombre, email))

        nuevo_id = cur.fetchone()[0]
        conn.commit()
        print(f"Usuario '{nombre}' creado con ID: {nuevo_id}")
    
    except Exception as e:
        print("Error al insertar:", e)
        conn.rollback()

def cerrar_conexion():
    cur.close()
    conn.close()
    print("Conexión Cerrada")