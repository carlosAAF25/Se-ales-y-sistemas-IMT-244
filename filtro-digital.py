import numpy as np
import librosa
import soundfile as sf  
from scipy.signal import butter, sosfilt

def butter_lowpass(cutoff, fs, order=5):
    sos = butter(order, cutoff, fs=fs, btype='low', output='sos')
    return sos

def apply_filter(data, cutoff, fs, order=5):
    sos = butter_lowpass(cutoff, fs, order=order)
    y = sosfilt(sos, data)
    return y

file_path = 'audio.wav' 
x, fs = librosa.load(file_path, sr=None) 

cutoff_hz = 1000.0   
order = 4            

x_filtered = apply_filter(x, cutoff_hz, fs, order)

x_norm = librosa.util.normalize(x_filtered)

output_path = 'audio_filtrado.wav'
sf.write(output_path, x_norm, fs)

print(f"Archivo guardado exitosamente como: {output_path}")