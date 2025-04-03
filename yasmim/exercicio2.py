import cv2

img1 = cv2.imread("lena.png")
img2 = cv2.imread("img_aluno.jpg")

negativo1 = 255 - img1
negativo2 = 255 - img2

cv2.imshow("Original Lena", img1)
cv2.imshow("Negativo Lena", negativo1)

cv2.imshow("Original Aluno", img2)
cv2.imshow("Negativo Aluno", negativo2)

cv2.imwrite("lena_negativo.jpg", negativo1)
cv2.imwrite("img_aluno_negativo.jpg", negativo2)

cv2.waitKey(0)
cv2.destroyAllWindows()
