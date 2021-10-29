import numpy as np
import cv2

retangulo = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(retangulo, (25, 25), (275, 275), 255, -1)
cv2.imshow("Retangulo", retangulo)

circulo = np.zeros((300, 300), dtype="uint8")
cv2.circle(circulo, (150, 150), 150, 255, -1)
cv2.imshow("Circulo", circulo)

bitwise_and = cv2.bitwise_and(retangulo, circulo)
cv2.imshow("AND", bitwise_and)
cv2.waitKey(0)

bitwise_or = cv2.bitwise_or(retangulo, circulo)
cv2.imshow("OR", bitwise_or)
cv2.waitKey(0)

bitwise_xor = cv2.bitwise_xor(retangulo, circulo)
cv2.imshow("XOR", bitwise_xor)
cv2.waitKey(0)

bitwise_not = cv2.bitwise_not(retangulo, circulo)
cv2.imshow("NOT", bitwise_not)
cv2.waitKey(0)