import cv2
import numpy as np

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainer/trainer.yml')

cascadePath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX
gstreamer_str = "sudo gst-launch-1.0 rtspsrc location=rtsp://192.168.1.55:8080/h264_ulaw.sdp latency=10 ! queue ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! videoscale ! appsink"
cam = cv2.VideoCapture(gstreamer_str, cv2.CAP_GSTREAMER)
yz=0
while True:
    
    ret, im =cam.read()

    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    for(x,y,w,h) in faces:

        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
     
        
        print(conf,"\t",Id)
        
        
        if(Id == 2 and conf < 50):
            Id1 = "Rohit Singh Rathore "
            
        else:
            Id1 = "New_Person "
            

        cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
        cv2.putText(im, str(Id1), (x,y-40), font, 2, (255,255,255), 3)

    cv2.imshow('im',im) 
    yt= "LTS/"
    yz=yz+1
    cv2.imwrite(yt+str(yz)+".jpg",image)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
