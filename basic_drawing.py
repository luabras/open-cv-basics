import numpy as np
import cv2

# inicializando um canvas de 300x300 com um espaco pro canal de 3 cores (rgb)
# o canvas eh preenchido com zeros, entao sua cor vai ser preta
canvas = np.zeros((300, 300, 3), dtype="uint8")

green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
white = (255, 255, 255)

# desenhando uma linha verde do canto superior esquerdo ate o canto inferior direito
cv2.line(canvas, (0, 0), (300, 300), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# desenhando uma linha vermelha com grossura 3 do superior direito ate o canto inferior esquerdo
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# desenhando um retangulo verde comecando no ponto (10, 10) e terminando no ponto (60, 60)
cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# desenhando um retangulo vermelho comecando no ponto (50, 200) e terminando no ponto (200, 250)
# a grossura da linha eh 5
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

# desenhando um retangulo azul comecando no ponto (200, 50) e terminando no ponto (225, 125)
# usando o valor -1 ou cv2.FILLED eh possivel preencher o retangulo
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")
(h, w) = canvas.shape[:2]
(centerX, centerY) = (w // 2, h // 2)

# aumentando o raio de 0 a 175, incrementando 25
for raio in range(0, 175, 25):
    # desenhando um circulo branco no centro com o raio atual
    cv2.circle(canvas, (centerX, centerY), raio, white)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)

canvas = np.zeros((300, 300, 3), dtype="uint8")

# desenhando 25 circulos
for i in range(0, 25):
    # pegando valores aleatorios para o raio, a cor e o ponto inicial de cada circulo
    raio = np.random.randint(5, high=200)
    cor = np.random.randint(0, high=256, size=(3,)).tolist()
    ponto = np.random.randint(0, high=300, size=(2,))
    # desenhando o circulo definido
    cv2.circle(canvas, tuple(ponto), raio, cor, -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)