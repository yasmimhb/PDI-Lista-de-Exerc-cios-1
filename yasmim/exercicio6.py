import cv2
import numpy as np
import matplotlib.pyplot as plt

def separar_planos_bits(img):
    planos = []
    for i in range(8):
        plano = ((img >> i) & 1) * 255
        planos.append(plano.astype(np.uint8))
    return planos

# Carregar imagens em escala de cinza
img_lena = cv2.imread("lena.png", cv2.IMREAD_GRAYSCALE)
img_aluno = cv2.imread("img_aluno.jpg", cv2.IMREAD_GRAYSCALE)

# Separar os planos de bits
planos_lena = separar_planos_bits(img_lena)
planos_aluno = separar_planos_bits(img_aluno)

# Plotar os planos de bits da Lena
fig1, axes1 = plt.subplots(2, 4, figsize=(12, 6))
fig1.suptitle("Planos de Bits - Lena", fontsize=16)

for i in range(8):
    row, col = divmod(i, 4)
    axes1[row, col].imshow(planos_lena[i], cmap='gray')
    axes1[row, col].set_title(f"Bit {i}")
    axes1[row, col].axis('off')

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()

# Plotar os planos de bits da imagem do aluno
fig2, axes2 = plt.subplots(2, 4, figsize=(12, 6))
fig2.suptitle("Planos de Bits - img_aluno", fontsize=16)

for i in range(8):
    row, col = divmod(i, 4)
    axes2[row, col].imshow(planos_aluno[i], cmap='gray')
    axes2[row, col].set_title(f"Bit {i}")
    axes2[row, col].axis('off')

plt.tight_layout()
plt.subplots_adjust(top=0.88)
plt.show()
