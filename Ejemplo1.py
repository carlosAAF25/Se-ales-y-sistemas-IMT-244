import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000)

# señal compuesta
x = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*10*t)

plt.plot(t,x)
plt.title("Señal compuesta")
plt.show()