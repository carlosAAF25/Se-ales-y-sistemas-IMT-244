import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

b =[0.5,1.0]
a=[1.0, -0.95]
polos = np.roots(a)
magnitudes = np.abs(polos)

def plot_zplane(b, a):
    z, p, k = signal.tf2zpk(b, a)
    
    plt.figure(figsize=(6, 6))
    unit_circle = plt.Circle((0,0), 1, color='red', fill=False, linestyle='--', label='Límite de Estabilidad')
    plt.gca().add_artist(unit_circle)
    
    plt.scatter(np.real(z), np.imag(z), s=50, marker='o', facecolors='none', edgecolors='blue', label='Ceros')
    plt.scatter(np.real(p), np.imag(p), s=50, marker='x', color='blue', label='Polos')
    
    plt.axhline(0, color='black', lw=1)
    plt.axvline(0, color='black', lw=1)
    plt.xlabel('Real')
    plt.ylabel('Imaginario')
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.show()

plot_zplane(b, a)