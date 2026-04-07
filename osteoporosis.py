import numpy as np
import matplotlib.pyplot as plt
import cv2

def procesar_roi_hueso(ruta, tamano_roi=256):
    img = cv2.imread(ruta, 0)
    h, w = img.shape
    centro_y, centro_x = h // 2, w // 2
    
    roi = img[centro_y - tamano_roi//2 : centro_y + tamano_roi//2, 
              centro_x - tamano_roi//2 : centro_x + tamano_roi//2]
    
    roi = (roi - np.min(roi)) / (np.max(roi) - np.min(roi))
    
    f_shift = np.fft.fftshift(np.fft.fft2(roi))
    magnitud = np.log(np.abs(f_shift) + 1)
    
    return roi, magnitud, f_shift

def perfil_radial(mag):
    y, x = np.indices(mag.shape)
    centro = np.array(mag.shape) // 2
    r = np.sqrt((x - centro[1])**2 + (y - centro[0])**2).astype(int)
    tbin = np.bincount(r.ravel(), mag.ravel())
    nr = np.bincount(r.ravel())
    return tbin / nr

roi_s, mag_s, _ = procesar_roi_hueso('hueso_sano.png')
roi_o, mag_o, _ = procesar_roi_hueso('hueso_osteo.png')

p_sano = perfil_radial(mag_s)
p_osteo = perfil_radial(mag_o)

fig, axs = plt.subplots(2, 3, figsize=(16, 10))

axs[0, 0].imshow(roi_s, cmap='gray')
axs[0, 0].set_title("ROI Hueso Sano")
axs[0, 1].imshow(mag_s, cmap='magma')
axs[0, 1].set_title("Espectro ROI Sano")
axs[0, 2].plot(p_sano[:120], label='Sano', color='blue', lw=2)
axs[0, 2].set_ylim(2, 12)
axs[0, 2].legend()

axs[1, 0].imshow(roi_o, cmap='gray')
axs[1, 0].set_title("ROI Hueso Osteoporosis")
axs[1, 1].imshow(mag_o, cmap='magma')
axs[1, 1].set_title("Espectro ROI Osteo")
axs[1, 2].plot(p_osteo[:120], label='Osteoporosis', color='red', lw=2)
axs[1, 2].set_ylim(2, 12)
axs[1, 2].legend()

plt.tight_layout()
plt.show()