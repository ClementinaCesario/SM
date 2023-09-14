import cv2
import numpy as np

# Defina uma cor em formato RGB (faça as substituições pelos valores desejados)
cor_rgb = np.array([[[255, 0, 0]]], dtype=np.uint8)  # Exemplo: vermelho puro (RGB)

# Converta a cor de RGB para YUV
cor_yuv = cv2.cvtColor(cor_rgb, cv2.COLOR_RGB2YUV)

# Extraia os componentes YUV da cor
Y = cor_yuv[0][0][0]  # Luminância (Y)
U = cor_yuv[0][0][1]  # Crominância U
V = cor_yuv[0][0][2]  # Crominância V

# Imprima os valores YUV
print(f"Luminância (Y): {Y}")
print(f"Crominância U: {U}")
print(f"Crominância V: {V}")