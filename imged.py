
import cv2
import numpy as np
import matplotlib.pyplot as plt

img_color = cv2.imread('imagenColor.jpg')
if img_color is None:
    raise FileNotFoundError("No se encontró 'imagenColor.jpg'")

img_rgb = cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB)

channels = cv2.split(img_rgb)
channel_names = ['Rojo (R)', 'Verde (G)', 'Azul (B)']
magnitude_spectrums = []

plt.figure(figsize=(18, 9))

plt.subplot(2, 4, 1)
plt.imshow(img_rgb)
plt.title('Imagen Color Original'), plt.axis('off')

for i, ch in enumerate(channels):
    plt.subplot(2, 4, i + 2)
    plt.imshow(ch, cmap='gray')  
    plt.title(f'Canal {channel_names[i]}'), plt.axis('off')

for i, ch in enumerate(channels):
    f_ch = np.fft.fft2(ch)
    fshift_ch = np.fft.fftshift(f_ch)
    mag_ch = 20 * np.log(np.abs(fshift_ch) + 1)
    magnitude_spectrums.append(mag_ch)

mag_rgb_vis = cv2.merge(magnitude_spectrums) 
plt.subplot(2, 4, 5)
plt.imshow(mag_rgb_vis.astype(np.uint8))
plt.title('Espectro Merged (Visualización RGB)'), plt.axis('off')

for i, mag in enumerate(magnitude_spectrums):
    plt.subplot(2, 4, i + 6)
    plt.imshow(mag, cmap='gray')  
    plt.title(f'Espectro Canal {channel_names[i]}'), plt.axis('off')

plt.tight_layout()  
plt.show()