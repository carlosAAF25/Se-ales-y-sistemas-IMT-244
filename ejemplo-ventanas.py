import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window

# 1. Configuración: 1 segundo de señal a 1000 Hz
fs = 1000 
t = np.linspace(0, 1, fs, endpoint=False)
N = len(t)

# Creamos dos señales:
# f1 = 5 Hz (perfecta, no causa leakage)
# f2 = 10.5 Hz (causa leakage porque no es entera en 1 segundo)
x = 1.0 * np.sin(2*np.pi*5*t) + 0.5 * np.sin(2*np.pi*10.5*t)

# 2. Definimos las ventanas a comparar
window_types = ['boxcar', 'hann', 'hamming', 'blackman']
labels = ['Rectangular', 'Hann', 'Hamming', 'Blackman']
colors = ['blue', 'orange', 'green', 'purple']

plt.figure(figsize=(12, 10))

# Subplot 1: Espectro Completo (Lineal)
plt.subplot(2,1,1)
for win, label, color in zip(window_types, labels, colors):
    w = get_window(win, N)
    X_fft = np.fft.fft(x * w)
    mag = np.abs(X_fft[:N//2]) * 2 / N # Normalización
    plt.plot(np.fft.fftfreq(N, 1/fs)[:N//2], mag, label=label, color=color, linewidth=2)

plt.title("Espectro Lineal: Las 'Montañas' de Fuga", fontsize=14)
plt.ylabel("Amplitud")
plt.xlim(0, 20)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

# Subplot 2: Zoom a la base (Donde vive el Leakage)
plt.subplot(2,1,2)
for win, label, color in zip(window_types, labels, colors):
    w = get_window(win, N)
    X_fft = np.fft.fft(x * w)
    mag = np.abs(X_fft[:N//2]) * 2 / N
    plt.plot(np.fft.fftfreq(N, 1/fs)[:N//2], mag, label=label, color=color, linewidth=2)

plt.title("Zoom a la base: Observen la 'suciedad' de la Rectangular (Azul)", fontsize=14)
plt.ylabel("Amplitud (Zoom)")
plt.xlabel("Frecuencia [Hz]")
plt.xlim(0, 20)
plt.ylim(0, 0.1) # Zoom agresivo a la base para ver el leakage
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()

plt.tight_layout()
plt.show()