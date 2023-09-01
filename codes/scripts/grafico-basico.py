r"""

Realizar uma simples plotagem com o matplot lib

"""
__author__ = "Marcel Barreto"

from matplotlib import pyplot as plt # Vizualizar

x = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29]
y = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]

# Inserir os dados no gráfico
plt.plot(x, y, c='green')

plt.title("Titulo")
plt.ylabel("Titulo y")
plt.xlabel("Titulo X")

plt.show()