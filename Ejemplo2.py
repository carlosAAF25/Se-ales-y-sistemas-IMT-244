
import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T = 2   
t = np.linspace(0, T, T * fs)

senal_util = 1.0 * np.sin(2 * np.pi * 1 * t)
senal_ruido = 0.3 * np.sin(2 * np.pi * 60 * t)
senal_con_ruido = senal_util + senal_ruido

x_fft = np.fft.fft(senal_con_ruido)


frecuencias = np.fft.fftfreq(len(senal_con_ruido), 1/fs)
n = len(senal_con_ruido) // 2
magnitud = np.abs(x_fft[:n]) * 2 / len(senal_con_ruido)


plt.figure(figsize=(10, 14))
# plt.plot(t, senal_con_ruido, color='purple')
# plt.title("Señal con Ruido (Vista en el Tiempo)")
plt.plot(frecuencias[:n], magnitud, color='green')
plt.title("Análisis de Fourier (Vista en Frecuencia)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.xlim(0, 80)
plt.grid(True)
plt.show()
















