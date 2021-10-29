import cv2

path = "C:/pyimage/OpenCV 101 - OpenCV Basics/imagens/teste.jpg"

img = cv2.imread(path)

cv2.circle(img, (168, 168), 90, (0, 0, 255), 2)
cv2.circle(img, (150, 164), 10, (0, 0, 255), -1)
cv2.circle(img, (192, 174), 10, (0, 0, 255), -1)

cv2.rectangle(img, (134, 200), (186, 218), (0, 0, 255), -1)

cv2.imshow("Output", img)
cv2.waitKey(0)