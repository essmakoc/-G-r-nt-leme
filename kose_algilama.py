import cv2
import matplotlib.pyplot as plt
import numpy as np 

img = cv2.imread("C:/Users/ASUS/.spyder-py3/Image processing/sudoku.jpg", 0)
img = np.float32(img)
plt.figure()
plt.axis("off")
plt.imshow(img, cmap = "gray")

# harris corner detection
"""
    blockSize = komşuluk boyutu
    ksize = kutucuk boyutu
    k = harris corner detection paremetre
"""
dst = cv2.cornerHarris(img, blockSize = 2, ksize = 3, k = 0.04)
plt.figure()
plt.axis("off")
plt.imshow(dst, cmap = "gray")

dst = cv2.dilate(dst, None)
img[dst > 0.2*dst.max()] = 1
plt.figure()
plt.axis("off")
plt.imshow(dst, cmap = "gray")

#shi tomasi detection
img = cv2.imread("C:/Users/ASUS/.spyder-py3/Image processing/sudoku.jpg", 0)
img = np.float32(img)
"""
    maxCorners = kac kose
    qualityLevel = 
    minDistance =iki kose arasındaki minimum distance
"""
corners = cv2.goodFeaturesToTrack(img, maxCorners = 100, qualityLevel = 0.01, minDistance = 10)
corners = np.int64(corners)

for i in corners:
    x, y = i.ravel()
    #img, center, radius, color
    cv2.circle(img, (x, y), 3, (125, 125, 125), cv2.FILLED)


plt.axis("off")
plt.imshow(img)