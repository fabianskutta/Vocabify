import numpy as np
import matplotlib.pyplot as plt

# Übergangsmatrizen
M_g = np.array([[0.3, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0.3, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0.3, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0.3, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0.3, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0.3, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0.3, 0, 0.7, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0.3, 0, 0.7, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0.7, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0.7, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0.7, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0.7, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0.7, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0.7, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0.7],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0.7]])

M_k = np.array([[0.8, 0.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0.75, 0, 0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0.7, 0, 0.3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0.65, 0, 0.35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0.6, 0, 0.4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0.55, 0, 0.45, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0.5, 0, 0.5, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0.45, 0, 0.55, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0.4, 0, 0.6, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0.35, 0, 0.65, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3, 0, 0.7, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0, 0.75, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0.8, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.15, 0, 0.85, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.1, 0, 0.9],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.01, 0.99]])

# Anfangsverteilung
initial_distribution = np.array([[658, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])

# Anzahl der Schritte in der Simulation
num_steps = 10000

# Simulationsschleife
distribution_g = initial_distribution
distribution_k = initial_distribution
for _ in range(num_steps):
    distribution_g = np.dot(distribution_g, M_g)
    distribution_k = np.dot(distribution_k, M_k)

# Ergebnisse als Matrix ausgeben
np.set_printoptions(suppress=True, precision=2)
print("Ergebnisse der Simulation:")
print("Gleichbleibende Wahrscheinlichkeit:")
print(distribution_g)
print("\nKontinuierlich ansteigende Wahrscheinlichkeit:")
print(distribution_k)

# Visualisierung der Ergebnisse als Balkendiagramm
x = np.arange(1, len(distribution_g[0]) + 1)  # Fachnummern von 1 bis 16
width = 0.35  # Breite der Balken

fig, ax = plt.subplots()
bars_g = ax.bar(x - width/2, distribution_g[0], width, label='Gleichbleibende Wahrscheinlichkeit')
bars_k = ax.bar(x + width/2, distribution_k[0], width, label='Kontinuierlich ansteigende Wahrscheinlichkeit')

ax.set_xlabel('Fach')
ax.set_ylabel('Verteilung')
ax.set_title('Verteilung der Vokabeln in den Fächern nach ' + str(num_steps) +' Durchgängen')
ax.set_xticks(x)
ax.legend()

plt.show()
