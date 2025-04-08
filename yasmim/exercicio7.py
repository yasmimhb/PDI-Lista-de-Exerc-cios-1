import cv2
import numpy as np
import matplotlib.pyplot as plt

# Funções dos algoritmos
def histograma(img_gray):
    hist = cv2.calcHist([img_gray], [0], None, [256], [0, 256])
    return hist.flatten()

def histograma_normalizado(hist, total_pixels):
    return hist / total_pixels

def histograma_acumulado(hist):
    return np.cumsum(hist)

def histograma_acumulado_normalizado(hist_acum):
    return hist_acum / hist_acum[-1]

# (i) Converter unequalized para cinza e gerar histograma (A)
img_uneq = cv2.imread("unequalized.jpg")
img_uneq_gray = cv2.cvtColor(img_uneq, cv2.COLOR_BGR2GRAY)
hist_uneq = histograma(img_uneq_gray)

plt.figure(figsize=(6,4))
plt.plot(hist_uneq, color='black')
plt.title("Histograma - unequalized (Cinza)")
plt.xlabel("Intensidade")
plt.ylabel("Frequência")
plt.grid()
plt.tight_layout()
plt.show()

# (ii) Histograma RGB de img_aluno
img_aluno = cv2.imread("img_aluno.jpg")
cores = ['b', 'g', 'r']
plt.figure(figsize=(6,4))
for i, cor in enumerate(cores):
    hist = cv2.calcHist([img_aluno], [i], None, [256], [0,256])
    plt.plot(hist, color=cor, label=f"Canal {cor.upper()}")
plt.title("Histograma - img_aluno (RGB)")
plt.xlabel("Intensidade")
plt.ylabel("Frequência")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

# (iii) img_aluno cinza: A, B, C, D
img_aluno_gray = cv2.cvtColor(img_aluno, cv2.COLOR_BGR2GRAY)
hist_a = histograma(img_aluno_gray)
hist_b = histograma_normalizado(hist_a, img_aluno_gray.size)
hist_c = histograma_acumulado(hist_a)
hist_d = histograma_acumulado_normalizado(hist_c)

# Plotar tudo
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

axs[0, 0].plot(hist_a, color='black')
axs[0, 0].set_title("A. Histograma")
axs[0, 0].set_xlim([0, 256])

axs[0, 1].plot(hist_b, color='gray')
axs[0, 1].set_title("B. Histograma Normalizado")
axs[0, 1].set_xlim([0, 256])

axs[1, 0].plot(hist_c, color='blue')
axs[1, 0].set_title("C. Histograma Acumulado")
axs[1, 0].set_xlim([0, 256])

axs[1, 1].plot(hist_d, color='red')
axs[1, 1].set_title("D. Histograma Acumulado Normalizado")
axs[1, 1].set_xlim([0, 256])

for ax in axs.flat:
    ax.set_xlabel("Intensidade")
    ax.set_ylabel("Frequência")
    ax.grid()

plt.tight_layout()
plt.show()
