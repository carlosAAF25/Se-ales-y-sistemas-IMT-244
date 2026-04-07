import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

FS = 1000          
N = 1024          
T = 1.0 / FS     

def get_sensor_data(start_time):
    t = np.linspace(start_time, start_time + N*T, N, endpoint=False)
    # Señal: 50Hz (ruido de red) + 120Hz (vibración mecánica) + Ruido blanco
    signal = 0.5 * np.sin(2 * np.pi * 50 * t) + 1.2 * np.sin(2 * np.pi * 120 * t)
    noise = np.random.normal(0, 0.5, N)
    return t, signal + noise

window = np.hanning(N)

current_time = 0
for i in range(10):  
    t, x = get_sensor_data(current_time)
    xf = fftfreq(N, T)[:N//2]
    yf = fft(x * window)  
    amplitude = 2.0/N * np.abs(yf[0:N//2])
    
  
    
    current_time += (N*T) / 2  # Desplazamos la ventana (50% de solapamiento)
    print(f"Procesado bloque {i}: Frecuencia dominante detectada.")