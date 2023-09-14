import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregue a imagem
imagem = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE)

# Calcule o histograma
histograma = cv2.calcHist([imagem], [0], None, [256], [0, 256])

# Plote o histograma
plt.hist(imagem.ravel(), 256, [0, 256])
plt.title('Histograma da Imagem')
plt.xlabel('Valor dos Pixels')
plt.ylabel('Frequência')
plt.show()