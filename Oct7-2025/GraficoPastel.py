import matplotlib.pyplot as plt

categorias = ["YouTube","Facebook", "WhatsApp", "TikTok"]
porcentajes = [1, 3, 2, 4]

plt.pie(
    porcentajes,
    labels=categorias,
    autopct="%1.1f%%",
    startangle=90,
)

plt.title("¿Que red social usas más?")
plt.show()