import numpy as np
import matplotlib.pyplot as plt

fs = 1000
T = 2
t = np.linspace(0, T, int(T * fs), endpoint=False)

senal_util = 1.0 * np.sin(2 * np.pi * 1 * t)
senal_ruido = 0.3 * np.sin(2 * np.pi * 60 * t)
senal_con_ruido = senal_util + senal_ruido

x_fft = np.fft.fft(senal_con_ruido)
frecuencias = np.fft.fftfreq(len(t), 1/fs)

x_fft_filtrada = x_fft.copy()
frecuencia_a_borrar = 60
margen = 1 

indices = np.where(np.abs(np.abs(frecuencias) - frecuencia_a_borrar) < margen)
x_fft_filtrada[indices] = 0

senal_reconstruida = np.fft.ifft(x_fft_filtrada).real

n = len(t) // 2
magnitud_original = np.abs(x_fft[:n]) * 2 / len(t)
magnitud_filtrada = np.abs(x_fft_filtrada[:n]) * 2 / len(t)

plt.figure(figsize=(10, 10))

plt.subplot(3, 1, 1)
plt.plot(t, senal_con_ruido, color='purple', alpha=0.3)
plt.plot(t, senal_reconstruida, color='blue')
plt.title("Tiempo: Original vs Filtrada")
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(frecuencias[:n], magnitud_original, color='red', alpha=0.5)
plt.title("Frecuencia: Antes del borrado")
plt.xlim(0, 80)
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(frecuencias[:n], magnitud_filtrada, color='green')
plt.title("Frecuencia: Después del borrado")
plt.xlim(0, 80)
plt.grid(True)

plt.tight_layout()
plt.show()