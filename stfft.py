import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 44100  
duracion = 2.0  
t = np.linspace(0, duracion, int(fs * duracion))

 
audio = signal.chirp(t, f0=440, f1=880, t1=duracion, method='linear')

audio += np.random.normal(0, 0.05, audio.shape)

f, t_spec, Zxx = signal.stft(audio, fs, nperseg=1024)

plt.figure(figsize=(10, 6))
plt.pcolormesh(t_spec, f, np.abs(Zxx), vmin=0, vmax=0.1, shading='gouraud')

plt.title('Espectrograma de la Señal (STFT)')
plt.ylabel('Frecuencia [Hz]')
plt.xlabel('Tiempo [seg]')
plt.ylim(0, 2000) 
plt.colorbar(label='Intensidad')
plt.show()