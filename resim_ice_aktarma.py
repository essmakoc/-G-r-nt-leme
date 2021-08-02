import cv2

img = cv2.imread("brad_pitt.jpg",0) # Sıfır resmi grayscale yapar 
cv2.imshow('image',img)


k = cv2.waitKey(0) &0xFF

if k == 27:   #wsc
    cv2.destroyAllWindows()
    
elif k == ord('s'):
    cv2.imwrite("brad_pitt_gray.jpg", img)
    cv2.destroyAllWindows()
