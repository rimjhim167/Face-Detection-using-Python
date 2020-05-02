# Face-Detection-using-Python

Face Detection is an application of machine learning. 

## Requirements
- Python3
- OpenCV, a Python library
- facemodel file

## Install

1. For this, a python library name opencv is required. Click [OpenCV](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html) to read more about this library.
```
pip install opencv-python
```
2. After installing openCV, download facemodel file from [here](cb.lk/facemodel). This xml file will help to do the frontal face detection.

## Coding

```
import cv2 
```
This will import openCV.
```
cam= cv2.VideoCapture(0)
face_detector= cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
```
The VideoCapture function of cv2 will cature video from the web camera. The argument 0 is for front camera.

```
while True: #using infinte loop, until user will press 'q', window will not be destroyed
    ret, frame= cam.read() #ret is an indicator, reading the camera
    if ret == False: # ret will be false if the image is not read.
        continue
        
    faces= face_detector.detectMultiScale(frame) #can get lot of faces
    for f in faces: 
        x,y,w,h= f # all faces will have 4 (x, y, w, h) co-ordinates
        cv2.rectangle(frame, (x,y), (x+y, y+h), (255, 255, 255), 2) #plotted a rectangle using (x,y) and (x+y,y+h ) co-ordinates. 2 is thickness of rectangle
        
    cv2.imshow("my face detection", frame)
    key_pressed= cv2.waitKey(1) & 0xFF #for keypressing, wait for 1 millisec.  
    if key_pressed == ord('q'): # will break on q key pressed
        break
cam.release()
cv2.destroyAllWindows() #to release the camera resource.
```
  
 ## Contribution
    
 Submit issues for bug reports or any enhancement ideas.
