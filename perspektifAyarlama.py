import cv2
import numpy as np


img = cv2.imread("C:/Users/ASUS/.spyder-py3/Image processing/kart.png", 0)
cv2.imshow("Orijinal Resim", img)

print(img.shape)


width = 400
height = 500

p1 = np.float32([[230, 1],[1, 472], [540, 150], [338, 617]])
p2 = np.float32([[0, 0], [0, height], [width,0], [width, height]])

matrix = cv2.getPerspectiveTransform(p1, p2)
print(matrix)

imgOutput = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("Cevirilmiş Resim", imgOutput)