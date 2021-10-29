import imutils
import cv2

path = "C:/pyimage/OpenCV 101 - OpenCV Basics/imagens/teste.jpg"

img = cv2.imread(path)
cv2.imshow("Original", img)
cv2.waitKey(0)

(h, w) = img.shape[:2]

# vamos mudar a largura para 150, entao vamos calcular o aspect ratio da nova largura
# para que a imagem n fique desproporcional
ratio = 150.0 / w
dim = (150, int(h * ratio))

resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (width)", resized)
cv2.waitKey(0)

# resize usando a algura 50
ratio2 = 50.0 / h
dim2 = (int(w * ratio2), 50)

resized2 = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized2)
cv2.waitKey(0)

resized = imutils.resize(img, width=100)
cv2.imshow("Resized via imutils", resized)
cv2.waitKey(0)