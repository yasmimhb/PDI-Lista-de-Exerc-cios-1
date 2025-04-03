import cv2
import numpy as np

def operador_potencia(img, gamma=1.5):
    img = img.astype(np.float32) / 255.0
    
    img_gamma = np.power(img, gamma) * 255.0  
    
    return img_gamma.astype(np.uint8)

img1 = cv2.imread("lena.png")
img2 = cv2.imread("img_aluno.jpg")

gamma_value = 1.5  
img1_gamma = operador_potencia(img1, gamma_value)
img2_gamma = operador_potencia(img2, gamma_value)

cv2.imshow("Original Lena", img1)
cv2.imshow(f"Gama {gamma_value} Lena", img1_gamma)

cv2.imshow("Original Aluno", img2)
cv2.imshow(f"Gama {gamma_value} Aluno", img2_gamma)

cv2.imwrite(f"lena_gama_{gamma_value}.jpg", img1_gamma)
cv2.imwrite(f"img_aluno_gama_{gamma_value}.jpg", img2_gamma)

cv2.waitKey(0)
cv2.destroyAllWindows()
