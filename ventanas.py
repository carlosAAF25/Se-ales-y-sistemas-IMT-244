import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import get_window

# Configuración
N = 128  # Usamos más puntos para una mejor visualización de la forma
windows = ['boxcar', 'hann', 'hamming', 'blackman']
titles = ['1. Ventana Rectangular (Por Defecto)', '2. Ventana de Hann (Suave)', '3. Ventana de Hamming (Equilibrada)', '4. Ventana de Blackman (Limpia)']
colors = ['blue', 'orange', 'green', 'purple']
explanations = ['No hay suavizado en los bordes. Máxima resolución, pero máximas fugas.', 'Suave transición a cero. Excelente equilibrio para la mayoría de los casos.', 'Similar a Hann, pero no llega a cero en los extremos (0.08).', 'La más suave en los extremos. Mínimas fugas, pero el pico más ancho.']

# Graficar cada ventana por separado
for i in range(4):
    w = get_window(windows[i], N)
    
    plt.figure(figsize=(10, 6))
    plt.plot(w, color=colors[i], linewidth=3)
    plt.title(titles[i], fontsize=14)
    plt.ylabel("Amplitud")
    plt.xlabel("Muestra")
    plt.grid(True, alpha=0.5)
    plt.ylim(-0.1, 1.1)
    plt.xlim(0, N-1)
    
    # Añadir texto de explicación
    plt.figtext(0.5, 0.01, explanations[i], ha="center", fontsize=12, bbox={"facecolor":"lightgray", "alpha":0.5, "pad":5})
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])  # Ajuste para el texto de explicación
    plt.show()