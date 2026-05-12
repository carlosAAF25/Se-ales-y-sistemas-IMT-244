t = np.linspace(0, 0.5, fs)
signal_10hz = np.sin(2 * np.pi * 10 * t)
noise_60hz = 0.5 * np.sin(2 * np.pi * 60 * t)
x = signal_10hz + noise_60hz