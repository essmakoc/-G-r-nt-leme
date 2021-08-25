import cv2
import numpy as np

img = cv2.imread("brad_pitt.jpg")
cv2.imshow("Orijinal ",img)
print(img.shape)

#boyutlandirma
imgResized = cv2.resize(img, (500, 600))
print("Yeni boyutlar: ", imgResized.shape)
cv2.imshow("Boyutlanmis Resim: ",imgResized)


#yatay
hor = np.hstack((imgResized, imgResized))
cv2.imshow("Horizontal", hor)

#dikey
ver =np.vstack((imgResized, imgResized))
cv2.imshow("Vertical", ver)