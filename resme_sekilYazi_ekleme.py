import cv2
import numpy as np

#siyah resim
img = np.ones((512, 512, 3), np.uint8)
print(img.shape)

cv2.imshow("Siyah", img)

#line
#resim, baslangic, bitis, renk, kalinlik
#normalde renk RGB -> opencv renk BGR
cv2.line(img, (0, 0), (512, 512), (0, 255, 0), 1) 
cv2.imshow("Cizgi", img)


#dikdortgen
#resim, baslangic, bitis, renk, kalinlik
cv2.rectangle(img, (0, 0), (256, 256), (255, 0, 0), 5)
cv2.imshow("dikdortgen", img)

#ic dolu dikdortgen
cv2.rectangle(img, (300, 300), (400, 400), (255, 0, 0), cv2.FILLED)
cv2.imshow("dolu dikdortgen", img)


#cember
#resim, merkez,yaricap, renk, kalinlik
cv2.circle(img, (100, 300), 25, (0, 0, 100), cv2.FILLED)
cv2.imshow("dolu cember", img)


#Metin
#img, text, org, fontFace, fontScale, color
cv2.putText(img, "Resim", (400, 400), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255))
cv2.imshow("Metin", img)