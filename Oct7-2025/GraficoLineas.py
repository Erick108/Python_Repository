import matplotlib.pyplot as plt

# Tema: ¿Cuantas horas dormistes anoche?
x = [2, 4, 5, 6, 7, 8]
y = [1, 1, 1, 1, 5, 1]

plt.plot(x, y, color="blue", linestyle="--", marker="o", label="Horas de sueño")
plt.title("¿Cuantas horas dormistes anoche?")
plt.xlabel("Frecuencia")
plt.ylabel("Horas")
plt.show()