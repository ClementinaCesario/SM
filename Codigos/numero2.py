import cv2
import numpy as np

# Definicao de uma cor em formato RGB (faça as substituições pelos valores desejados)
cor_rgb = np.array([[[0, 255, 0]]], dtype=np.uint8)  # Exemplo: verde puro (RGB)

# Convertendo a cor de RGB para HSV
cor_hsv = cv2.cvtColor(cor_rgb, cv2.COLOR_RGB2HSV)

# Extraindo os componentes HSV da cor
hue = cor_hsv[0][0][0]        # Matiz
saturation = cor_hsv[0][0][1]  # Saturação
value = cor_hsv[0][0][2]       # Valor (brilho)

# Imprimimindo os valores HSV
print(f"Hue (Matiz): {hue}")
print(f"Saturation (Saturação): {saturation}")
print(f"Value (Valor): {value}")
