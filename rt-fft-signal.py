import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.fft import fft, fftfreq

FS = 1000  
N = 1024
T = 1.0 / FS
xf = fftfreq(N, T)[:N//2]
window = np.hanning(N)

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
line1, = ax1.plot(np.arange(N), np.zeros(N), color='blue')  
line2, = ax2.plot(xf, np.zeros(N//2), color='red')        

ax1.set_ylim(-3, 3)
ax1.set_title("Señal del Sensor (Tiempo)")
ax2.set_ylim(0, 1)
ax2.set_title("Análisis Espectral (FFT)")
ax2.set_xlabel("Frecuencia (Hz)")

def update(frame):
    t_base = frame * 0.1
    t = np.linspace(t_base, t_base + N*T, N)
    
    signal = np.sin(2 * np.pi * 50 * t) + 1.5 * np.sin(2 * np.pi * 120 * t)
    noise = np.random.normal(0, 0.4, N)
    x = signal + noise
    
    yf = fft(x * window)
    amplitude = 2.0/N * np.abs(yf[:N//2])
    
    line1.set_ydata(x)
    line2.set_ydata(amplitude)
    return line1, line2

ani = FuncAnimation(fig, update, interval=50, blit=True)
plt.tight_layout()
plt.show()