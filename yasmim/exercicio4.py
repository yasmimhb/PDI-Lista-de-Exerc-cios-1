import cv2
import numpy as np

def operador_logaritmico(img):
    img = img.astype(np.float32)
    
    c = 255 / np.log(1 + np.max(img))
    
    img_log = c * np.log(1 + img)
    
    return img_log.astype(np.uint8)

img1 = cv2.imread("lena.png")
img2 = cv2.imread("img_aluno.jpg")

img1_log = operador_logaritmico(img1)
img2_log = operador_logaritmico(img2)

cv2.imshow("Original Lena", img1)
cv2.imshow("Log Lena", img1_log)

cv2.imshow("Original Aluno", img2)
cv2.imshow("Log Aluno", img2_log)

cv2.imwrite("lena_log.jpg", img1_log)
cv2.imwrite("img_aluno_log.jpg", img2_log)

cv2.waitKey(0)
cv2.destroyAllWindows()
