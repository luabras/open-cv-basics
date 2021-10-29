import numpy as np
import cv2
import imutils

path = "C:/pyimage/OpenCV 101 - OpenCV Basics/imagens/teste.jpg"

img = cv2.imread(path)

# pegando a altura e largura da imagem
(h, w) = img.shape[:2]

cv2.imshow("Original", img)
cv2.waitKey(0)

matriz = np.float32([[1, 0, 25], [0, 1, 50]])
shifted = cv2.warpAffine(img, matriz, (w, h))
cv2.imshow("Shifted Down and Right", shifted)
cv2.waitKey(0)

matriz2 = np.float32([[1, 0, -50], [0, 1, -90]])
shifted = cv2.warpAffine(img, matriz2, (w, h))
cv2.imshow("Shifted Up and Left", shifted)
cv2.waitKey(0)

shifted = imutils.translate(img, 0, 100)
cv2.imshow("Shifted Down", shifted)
cv2.waitKey(0)