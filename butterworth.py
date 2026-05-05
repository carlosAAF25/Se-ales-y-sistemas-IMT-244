import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000        
t = np.arange(0, 1.0, 1/fs)  

#Señal original: 5 Hz
clean_signal = np.sin(2 * np.pi * 5 * t)

#ruido de alta frecuencia: 120 Hz
noise = 0.5 * np.sin(2 * np.pi * 120 * t)
noisy_signal = clean_signal + noise

 
order = 4# Orden del filtro Butterworth
cutoff_freq = 30  #frecuencia de corte en Hz
nyquist = 0.5 * fs
normal_cutoff = cutoff_freq / nyquist# frecuencia normalizada



b, a = signal.butter(order, normal_cutoff, btype='low', analog=False)



filtered_signal = signal.lfilter(b, a, noisy_signal)












plt.figure(figsize=(12, 6))
plt.subplot(3, 1, 1)
plt.plot(t, clean_signal, label='Original (5 Hz)')
plt.title('Señal Original Limpia')
plt.grid(True)

plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal, color='red', alpha=0.7, label='Ruidosa (5Hz + 120Hz)')
plt.title('Señal con Ruido de Alta Frecuencia')
plt.grid(True)

plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal, color='green', label='Filtrada')
plt.title(f'Señal Recuperada (Butterworth LPF {cutoff_freq}Hz)')
plt.xlabel('Tiempo [s]')
plt.grid(True)

plt.tight_layout()
plt.show()


