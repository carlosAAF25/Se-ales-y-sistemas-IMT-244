import numpy as np
import matplotlib.pyplot as plt


fs = 1000 
t = np.linspace(0, 1, fs, endpoint=False)


x1 = np.sin(2*np.pi*5*t)   # 5 Hz
x2 = np.sin(2*np.pi*10*t)  # 10 Hz
x = x1 + x2                


N = len(x)
X_fft = np.fft.fft(x)                      
frecuencias = np.fft.fftfreq(N, 1/fs)      


n_mitad = N // 2
f_positivas = frecuencias[:n_mitad]
magnitud = np.abs(X_fft[:n_mitad]) * 2 / N 


plt.figure(figsize=(10, 12))

plt.subplot(4,1,1)
plt.plot(t, x1, color='blue')
plt.title("Señal 1 (5 Hz)")
plt.grid(True)

plt.subplot(4,1,2)
plt.plot(t, x2, color='orange')
plt.title("Señal 2 (10 Hz)")
plt.grid(True)

plt.subplot(4,1,3)
plt.plot(t, x, color='purple')
plt.title("Señal compuesta (Suma en el Tiempo)")
plt.grid(True)


plt.subplot(4,1,4)
plt.plot(f_positivas, magnitud, color='green', linewidth=2)
plt.title("Espectro de Frecuencias (FFT)")
plt.xlabel("Frecuencia [Hz]")
plt.ylabel("Amplitud")
plt.xlim(0, 20)  
plt.grid(True)

plt.tight_layout()
plt.show()

