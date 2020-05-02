import cv2
cam= cv2.VideoCapture(0)
face_detector= cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') 

while True: 
    ret, frame= cam.read() 
    if ret == False:
        continue
        
    faces= face_detector.detectMultiScale(frame)
    for f in faces: 
        x,y,w,h= f 
        cv2.rectangle(frame, (x,y), (x+y, y+h), (255, 255, 255), 2)
        
    cv2.imshow("my face detection", frame)
    key_pressed= cv2.waitKey(1) & 0xFF  
    if key_pressed == ord('q'): 
        break
cam.release()
cv2.destroyAllWindows()
