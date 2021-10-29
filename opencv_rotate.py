import imutils
import cv2

path = "C:/pyimage/OpenCV 101 - OpenCV Basics/imagens/teste.jpg"

img = cv2.imread(path)

# pegando a altura e largura da imagem
(h, w) = img.shape[:2]

cv2.imshow("Original", img)
cv2.waitKey(0)

(cX, cY) = (w // 2, h // 2)

# rotacionando a imagem 45 graus ao redor do centro

# getRotationMatrix2D recebe o ponto de rotacao, o grau de rotacao (anti horario) e a escala da imagem.
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)

# rotacionando a imagem -90 graus (horario) ao redor do centro
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)

# rotacionando a imagem a partir do ponto 10, 10
M = cv2.getRotationMatrix2D((10, 10), 45, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))
cv2.imshow("Rotated by Arbitrary Point", rotated)

# rotacionando com a lib imutils
rotated = imutils.rotate(img, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)

# rotacionando sem cortar a imagem
rotated = imutils.rotate_bound(img, -33)
cv2.imshow("Rotated Without Cropping", rotated)
cv2.waitKey(0)