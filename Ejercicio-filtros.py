import numpy as np
fs = 500.0         
duracion = 1.0      
t = np.arange(0, duracion, 1/fs)
ecg_limpio = (np.sin(2 * np.pi * 5 * t) + 
              0.5 * np.sin(2 * np.pi * 12 * t) + 
              0.2 * np.sin(2 * np.pi * 2 * t)) 
ruido_50hz = 0.8 * np.sin(2 * np.pi * 50 * t)
ecg_ruidoso = ecg_limpio + ruido_50hz