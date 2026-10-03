import numpy as np
import matplotlib.pyplot as plt

# Skapa ett rutnät (grid) av koordinater
x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
X, Y = np.meshgrid(x, y)

# Definiera systemet av differentialekvationer (x' och y')
U = -X + 3*Y
V = -3*X + 5*Y

# Skapa figuren
plt.figure(figsize=(8, 8))

# Rita strömlinjer för att få en snygg representation av fältet
plt.streamplot(X, Y, U, V, color='dodgerblue', linewidth=1.5, density=1.2, arrowsize=1.5)

# Rita ut egenvektorlinjen (y = x)
plt.plot([-4, 4], [-4, 4], 'r--', linewidth=2, label='Egenvektor $\\vec{K}$ (y = x)')

# Formatera plotten (axlar, rutnät, etc.)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)
plt.title('Fasporträtt: Instabil degenererad nod', fontsize=14)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left')

# Visa plotten direkt
plt.show()