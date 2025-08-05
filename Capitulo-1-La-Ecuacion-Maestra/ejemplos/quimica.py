# Oscilador molecular NaCl
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)
Na = np.sin(2*np.pi*1.5*t)
Cl = np.sin(2*np.pi*1.5*t + np.pi)
plt.plot(t, Na, label="Na+")
plt.plot(t, Cl, label="Cl-")
plt.title("Oscilación en fase opuesta NaCl")
plt.legend()
plt.grid()
plt.show()
