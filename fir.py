import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

 
fs = 1000      
t = np.arange(0, 0.5, 1/fs)   

 
f1, f2, f3 = 50, 150, 350
senal_pura = np.sin(2 * np.pi * f1 * t)
ruido = 0.5 * np.sin(2 * np.pi * f2 * t) + 0.3 * np.sin(2 * np.pi * f3 * t)
senal_compuesta = senal_pura + ruido

 
orden = 61  
f_corte = 80.0

coeficientes = signal.firwin(orden, f_corte, fs=fs, window='hamming')

# 4. Aplicación del filtro 
senal_filtrada = signal.lfilter(coeficientes, 1.0, senal_compuesta)

plt.figure(figsize=(12, 8))

plt.subplot(2, 1, 1)
plt.plot(t, senal_compuesta, label='Señal Compuesta (50Hz + 150Hz + 350Hz)', alpha=0.7)
plt.plot(t, senal_pura, 'r', label='Señal Original de 50Hz (Deseada)', linewidth=2)
plt.title('Señal Antes del Filtrado')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(t, senal_filtrada, 'g', label='Salida del Filtro FIR', linewidth=2)
plt.title(f'Señal Después del Filtrado (FIR Pasa-Bajos {f_corte}Hz)')
plt.xlabel('Tiempo [s]')
plt.ylabel('Amplitud')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()