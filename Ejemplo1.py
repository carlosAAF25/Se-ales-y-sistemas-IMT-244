import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000)
x = np.sin(2*np.pi*5*t) + np.sin(2*np.pi*10*t)

x1 = np.sin(2*np.pi*5*t)
x2= np.sin(2*np.pi*10*t)

plt.subplot(3,1,1)
plt.plot(t,x1)
plt.title("Señal 1 (5 Hz)")


plt.subplot(3,1,2)
plt.plot(t,x2)
plt.title("Señal 2 (10 Hz)")

plt.subplot(3,1,3)
plt.plot(t,x)
plt.title("Señal compuesta")
plt.show()

