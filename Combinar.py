import pandas as pd
import glob

# Lista de archivos .csv (ajusta la ruta si están en otra carpeta)
archivos = ["Datos-personales-1.csv", "Datos-personales-2.csv", "Datos-personales-3.csv", "Datos-personales-4.csv", "Datos-personales-5.csv"]
# O usa: archivos = glob.glob("*.csv")  # para todos los .csv en la carpeta actual

# Leer y concatenar
dfs = [pd.read_csv(f, low_memory=False) for f in archivos]
combinado = pd.concat(dfs, ignore_index=True)

# Guardar el resultado
combinado.to_csv("Datos_personales.csv", index=False)
print("✅ Archivos combinados en 'Datos_personales.csv'")