import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs=10
t = np.linspace(0, 1, fs)

# 1. Información Útil: Una oscilación de 15 Hz
clean = 1.0 * np.sin(2 * np.pi * 15 * t) 

# 2. Problema A: Deriva de línea base (0.5 Hz) -> Necesita HPF
drift = 2.0 * np.sin(2 * np.pi * 0.5 * t)

# 3. Problema B: Ruido de red eléctrica (50 Hz) -> Necesita BSF
interf = 0.8 * np.sin(2 * np.pi * 50 * t)

# 4. Problema C: Ruido de alta frecuencia (>150 Hz) -> Necesita LPF
noise = 0.5 * np.random.normal(size=len(t)) 

signal_raw = clean + drift + interf + noise