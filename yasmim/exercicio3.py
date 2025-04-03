import cv2
import numpy as np

def normalizar_contraste(img):
    img = img.astype(np.float32)
    
    min_val = np.min(img)
    max_val = np.max(img)
    
    img_norm = (img - min_val) / (max_val - min_val) * 255.0
    
    return img_norm.astype(np.uint8)

img1 = cv2.imread("lena.png")
img2 = cv2.imread("img_aluno.jpg")

img1_norm = normalizar_contraste(img1)
img2_norm = normalizar_contraste(img2)

cv2.imshow("Original Lena", img1)
cv2.imshow("Contraste Ajustado Lena", img1_norm)

cv2.imshow("Original Aluno", img2)
cv2.imshow("Contraste Ajustado Aluno", img2_norm)

cv2.imwrite("lena_contraste.jpg", img1_norm)
cv2.imwrite("img_aluno_contraste.jpg", img2_norm)

cv2.waitKey(0)
cv2.destroyAllWindows()
