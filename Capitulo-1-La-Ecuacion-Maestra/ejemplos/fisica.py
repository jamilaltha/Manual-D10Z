# Simulación TTA: velocidad de galaxia
import numpy as np
import matplotlib.pyplot as plt

r = np.linspace(0.1, 50, 100)
v = 200 * np.tanh(r / 10)
plt.plot(r, v)
plt.title("Curva de rotación TTA")
plt.xlabel("r (kpc)")
plt.ylabel("v (km/s)")
plt.grid()
plt.show()
 
