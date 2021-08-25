import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("C:/Users/ASUS/.spyder-py3/Image processing/abc.png", 0)
plt.figure(), plt.imshow(img, cmap = "gray"), plt.axis("off"), plt.title("Orijinal Resim"), plt.show()


"""
     -erozyon 
         ön plandaki nesnenin sınırlarını aşındırır.

"""      

kernel = np.ones((5, 5), dtype = np.uint8)  
result = cv2.erode(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result, cmap = "gray"), plt.axis("off"), plt.title("Erozyon Resim"), plt.show()



"""
    - Genişleme
        görüntüdeki beyaz bölgeyi arttırır.
"""

result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure(), plt.imshow(result2, cmap = "gray"), plt.axis("off"), plt.title("Genişleme Resim"), plt.show()


"""
    -   Açma
        erozyon + Genişleme
        beyaz gürültünün giderilmesinde faydalıdır.
"""
#whiteNoise

whiteNoise = np.random.randint(0, 2 , size = img.shape[:2])
whiteNoise = whiteNoise * 255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("White Noise"), plt.show()

noise_img = whiteNoise + img
plt.figure(), plt.imshow(noise_img, cmap = "gray"), plt.axis("off"), plt.title("Image with White Noise"), plt.show()

#Açma

opening = cv2.morphologyEx(noise_img.astype(np.float32()), cv2.MORPH_OPEN, kernel)
plt.figure(), plt.imshow(opening, cmap = "gray"), plt.axis("off"), plt.title("Acilma"), plt.show()

"""
    - Kapatma
        Genişleme + erozyon
        nesne üzerindeki küçük delikleri kapatmak 
        için kullanışlıdır
        
"""
#black Noise

blackNoise = np.random.randint(0, 2 , size = img.shape[:2])
blackNoise = blackNoise * -255
plt.figure(), plt.imshow(whiteNoise, cmap = "gray"), plt.axis("off"), plt.title("Black Noise"), plt.show()

black_noise_img = blackNoise + img
black_noise_img[black_noise_img <= -245] = 0

plt.figure(), plt.imshow(black_noise_img, cmap = "gray"), plt.axis("off"), plt.title("Black Noise Image"), plt.show()


#kapatma

closing = cv2.morphologyEx(black_noise_img.astype(np.float32()), cv2.MORPH_CLOSE, kernel)
plt.figure(), plt.imshow(closing, cmap = "gray"), plt.axis("off"), plt.title("Kapatma"), plt.show()

"""
    - Morfolojik Gradyan
        Genişleme ve erozyon arasındaki farktır

"""



gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure(), plt.imshow(gradient, cmap = "gray"), plt.axis("off"), plt.title("Gradyan"), plt.show()






