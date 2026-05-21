import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 250   
t = np.arange(0, 2.0, 1/fs)   

ritmo_alfa = 1.2 * np.sin(2 * np.pi * 10 * t)  # Onda a 10 Hz (Dentro del rango 8-12 Hz)
ritmo_beta = 0.6 * np.sin(2 * np.pi * 22 * t)  # Onda a 22 Hz (Dentro del rango 12-30 Hz)
eeg_real = ritmo_alfa + ritmo_beta
ruido_ojos = 4.0 * np.sin(2 * np.pi * 1 * t)      # Parpadeo de ojos (Muy baja frecuencia: 1 Hz)
ruido_musculos = 2.5 * np.sin(2 * np.pi * 40 * t)  # Movimiento del cuello (Alta frecuencia: 40 Hz)
# Señal cruda que recibe el microprocesador del casco
eeg_ruidoso = eeg_real + ruido_ojos + ruido_musculos

