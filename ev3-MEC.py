import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000
t = np.arange(0, 1.0, 1/fs) 
ruido_planta = 2.0 * np.sin(2 * np.pi * 10 * t) 
silbido_rodamiento = 1.0 * np.sin(2 * np.pi * 250 * t)
senal_microfono = ruido_planta + silbido_rodamiento + np.random.normal(0, 0.5, len(t))

 
 