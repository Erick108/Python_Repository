#Por: Erick Josué Rivera Velásquez
import pandas as pd

datos = pd.read_csv("Electric_Vehicle_Population_Data (1).csv")

#2. Informacion resumida del dataset
print(datos.describe())

#3. Identificar los tipos de datos de cada columna utilizando dtypes y qué tipo de análisis se puede hacer sobre esta información.
print("Tipos de datos en el dataset:")
print(datos.dtypes)
# Los tipos de datos que hay en nuestro dataset son: object, float64 e int64.
# Se puede hacer un analisis de tipo#

#4.1. Primer resultado
print("El primer dato es: ")
print(datos.head())

#4.2. Ultimo resultado
print("El ultimo dato es: ")
print(datos.tail())

#5. Ordenar los resultados
print("Resultados ordenados: ")
print(datos.sort_values)

#6. Seleccionar una columna y, calcular al menos dos de las siguientes medidas: 
# a. Media (np.mean()), b. Mediana (np.median()), c. Desviación estándar (np.std())#

print(datos.columns)
print(f"Distancia promedio que recorren los vehiculos electricos: {datos['Electric Range'].mean()}")
print(f"Mediana de la distancia que reccoren los vehiculos electricos: {datos['Electric Range'].median()}")
print(f"La desviación estandar de la distancia que reccoren los vehiculos electricos: {datos['Electric Range'].std()}")


# Interpretación de resultados. #
# a. Describe brevemente de qué trata el dataset utilizado 
# El dataset lleva registro de la adopcion y crecimiento de los vehiculos electricos atravez paises y regiones.#
# b. ¿Qué información permite ver el resumen estadístico? 
# El resumen estadistico me muestra los datos numericos mas relevantes del dataset, la media, la desviacion estandar, el minimo, el maximo, etc.#
# c. ¿Qué cambios o tendencias se detectan en la información del dataset? 
# Que la popularidad de los autos electricos va creciendo o por lo menos se mantiene ya que hay modelos para el año 2026
# lo que significa que el negocio de los autos electricos va bien. #
# d. ¿Qué categorías sobresalen en la comparación y por qué crees que será? 
# El Postal Code, Model Year, Electric Range, Dase MSRP, Legislative District, DOL Vehicle ID, 2020 Census Tract
# debido a que esos datos son los que aparecen en el resumen son los que mas sobresalen #
# e. ¿Qué diferencias se observan entre los primeros y últimos registros? 
# Honestamente, no logro identificar diferencias notables entre los primeros y los ultimos datos#
# f. ¿Qué aportan las medidas estadísticas al análisis del dataset? 
# Un conocimiento mas detallado sobre el promedio de dtos en el dataset#