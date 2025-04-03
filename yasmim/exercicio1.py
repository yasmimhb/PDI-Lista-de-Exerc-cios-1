import cv2

img1 = cv2.imread('lena.png', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('img_aluno.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Lena - Níveis de Cinza', img1)
cv2.imshow('Imagem Aluno - Níveis de Cinza', img2)

cv2.imwrite('lena_cinza.png', img1)
cv2.imwrite('img_aluno_cinza.png', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
