
import numpy as np
import matplotlib.pyplot as plt

senal_util = 1.0 * np.sin(2 * np.pi * 1 * t)
senal_ruido = 0.3 * np.sin(2 * np.pi * 60 * t)
senal_con_ruido = senal_util + senal_ruido
