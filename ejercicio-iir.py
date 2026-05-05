import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

fs = 1000
t = np.arange(0, 0.5, 1/fs)
clean = np.sin(2 * np.pi * 10 * t)
noise = 0.5 * np.sin(2 * np.pi * 150 * t)
x = clean + noise  