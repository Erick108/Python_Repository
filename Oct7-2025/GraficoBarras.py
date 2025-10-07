import matplotlib.pyplot as plt

# Tema: ¿Cuantas tasas de cafe tomas al dia?

categorias = ["1 tasa", "2 tasas", "3 tasas", "4 tasas", "5 tasas"]
valores = []

# Crear gráfico de barras
plt.bar(categorias, valores, color="brown")

# Personalización
plt.title("¿Cuantas tasas de cafe tomas al dia?")
plt.xlabel("Cantidad de tasas")
plt.ylabel("Frecuencia")
plt.ylim(0, 100)  # Límite del eje Y

# Mostrar
plt.show()