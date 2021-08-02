import cv2
import time


video_name = "MOT17-04-DPM.mp4"

cap = cv2.VideoCapture(video_name)

print("Genişlik: ", cap.get(3))
print("Yukseklik: ", cap.get(4))


#video kontrolu
if cap.isOpened() == False:
    print("video yüklemede hata oldu")
    
while True:
    ret, frame = cap.read()
    
    if ret == True:
        time.sleep(0.01) #video hız ayarı
        cv2.imshow("video", frame)
        
    else:
        break
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()