import numpy as np
import cv2

path = "C:/pyimage/OpenCV 101 - OpenCV Basics/imagens/teste.jpg"

img = cv2.imread(path)
cv2.imshow("Original", img)
cv2.waitKey(0)

(h, w) = img.shape[:2]

# construindo um array com a mesma dimensao da imagem original
mask_ret = np.zeros((h, w), dtype=np.uint8)
# desenhando um retangulo branco na regiao do canto inferior esquerdo (a regiao que queremos extrair)
cv2.rectangle(mask_ret, (0, 90), (290, 450), 255, -1)
cv2.imshow("Mascara retangular", mask_ret)
cv2.waitKey(0)

# aplicando a mascara
# mask=mask_ret retorna true quando os pixels das imagens de input sao iguais,
# e a mascara nao eh zero em cada coordenada (nesse caso, apenas pixels dentro da parte branca)
masked = cv2.bitwise_and(img, img, mask=mask_ret)
cv2.imshow("Imagem com a mascara", masked)
cv2.waitKey(0)

mask_circ = np.zeros((h, w), dtype=np.uint8)
cv2.circle(mask_circ, (145, 200), 100, 255, -1)
masked2 = cv2.bitwise_and(img, img, mask=mask_circ)

cv2.imshow("Mascara circular", mask_circ)
cv2.waitKey(0)
cv2.imshow("Imagem com a mascara", masked2)
cv2.waitKey(0)

