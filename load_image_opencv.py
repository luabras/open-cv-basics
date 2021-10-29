import cv2

path = "C:/pyimage/OpenCV 101 - OpenCV Basics/imagens/teste.jpg"

img = cv2.imread(path)

(h, w, c) = img.shape[:3]

print("largura: {} pixels".format(w))
print("altura: {} pixels".format(h))
print("canais: {}".format(c))

cv2.imshow("Imagem", img)
cv2.waitKey(0)

cv2.imwrite("imagem.png", img)

