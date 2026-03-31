import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window, freqz

# Configuración
N = 64 # Usamos pocos puntos para ver los lóbulos de frecuencia
windows = ['boxcar', 'hann', 'hamming', 'blackman'] # Boxcar es la rectangular
colors = ['blue', 'orange', 'green', 'purple']
labels = ['Rectangular', 'Hann', 'Hamming', 'Blackman']

plt.figure(figsize=(12, 10))

# --- GRÁFICA 1: DOMINIO DEL TIEMPO ---
plt.subplot(2,1,1)
for win_name, color, label in zip(windows, colors, labels):
    w = get_window(win_name, N)
    plt.plot(w, color=color, label=label, linewidth=2)
    
plt.title("Dominio del Tiempo: Formas de las Ventanas (N=64)")
plt.ylabel("Amplitud")
plt.xlabel("Muestra")
plt.grid(True, alpha=0.5)
plt.legend()
plt.ylim(-0.1, 1.1)

# --- GRÁFICA 2: DOMINIO DE LA FRECUENCIA (ESPECTRO) ---
# Aquí vemos cómo se 'ensucia' la frecuencia de la ventana
plt.subplot(2,1,2)
for win_name, color, label in zip(windows, colors, labels):
    w = get_window(win_name, N)
    
    # freqz calcula la respuesta en frecuencia de un filtro
    # Usamos esto para ver cómo la ventana altera la frecuencia
    w, h = freqz(w, worN=2048) # Más puntos para suavizar la curva de frecuencia
    
    # Convertir respuesta a Decibelios (dB) y normalizar el pico a 0dB
    response = 20 * np.log10(np.abs(h) / np.max(np.abs(h)) + 1e-10) # 1e-10 para evitar log(0)
    
    # Graficar en Decibelios (dB) vs Frecuencia Normalizada (pi radians/muestra)
    # w / np.pi va de 0 a 1, donde 1 es la frecuencia de Nyquist (fs/2)
    plt.plot(w / np.pi, response, color=color, label=label, linewidth=2)

plt.title("Dominio de la Frecuencia: Comparación de Fugas (Leakage) en dB")
plt.ylabel("Amplitud Normalizada [dB]")
plt.xlabel("Frecuencia Normalizada [π rad/muestra] (1 = Nyquist)")
plt.grid(True, alpha=0.5)
plt.legend()
plt.ylim(-100, 5) # Zoom para ver los lóbulos laterales

plt.tight_layout()
plt.show()