import cv2

path = "C:/pyimage/OpenCV 101 - OpenCV Basics/imagens/teste.jpg"

img = cv2.imread(path)

# pegando a altura e largura da imagem
(h, w) = img.shape[:2]

cv2.imshow("Original", img)

#------------------------------------------------------------------------------#

# formato eh imagem[y, x]

# acessando o pixel (0, 0) da imagem (que eh o canto superior esquerdo)
(b, g, r) = img[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# acessando o pixel em x=50 e y=20 da imagem
(b, g, r) = img[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# colocando o pixel em x=50 e y=20 na cor vermelha
img[20, 50] = (0, 0, 255)
(b, g, r) = img[20, 50]
print("Pixel at (50, 20) - Red: {}, Green: {}, Blue: {}".format(r, g, b))

# calculando o centro da imagem dividindo a altura e a largura por 2
(cX, cY) = (w // 2, h // 2)

# usando slice de array do numpy pra pegar a regiao superior esquerda da imagem
tl = img[0:cY, 0:cX]
cv2.imshow("regiao superior esquerda", tl)

# pegando a regiao superior direita da imagem
tr = img[0:cY, cX:w]
# pegando a regiao inferior direita da imagem
br = img[cY:h, cX:w]
# pegando a regiao inferior esquerda da imagem
bl = img[cY:h, 0:cX]
cv2.imshow("regiao superior direita", tr)
cv2.imshow("regiao inferior direita", br)
cv2.imshow("regiao inferior esquerda", bl)

# setando a cor da regiao superior esquerda da imagem para verde
img[0:cY, 0:cX] = (0, 255, 0)

cv2.imshow("Atualizada", img)
cv2.waitKey(0)