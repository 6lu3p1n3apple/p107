import cv2
import math

b1=530
b2=300

xpos=[]
ypos=[]

video = cv2.VideoCapture("footvolleyball.mp4")

tracker = cv2.TrackerCSRT_create()

ret,img=video.read()
bbox=cv2.selectROI("select bounding box",img,False)

tracker.init(img,bbox)

def drawbox(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3,1)
    cv2.putText(img,"TRACKING",(75,90),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2) 

def goaltrack(img,bbox):
    x,y,w,h=int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])
    c1=x+int(w/2)
    c2=y+int(h/2)
    cv2.circle(img,(c1,c2),2,(0,255,0),5)
    cv2.circle(img,(int(b1),int(b2)),2,(0,0,255),4)

    dist=math.sqrt(((c1-b1)**2)+((c2-b2)**2))
    if dist<=20:
        cv2.putText(img,"GOAL",(300,90),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2) 

    xpos.append(c1)
    ypos.append(c2)

    for i in range(len(xpos)-1):
        cv2.circle(img,(xpos[i],ypos[i]),2,(255,0,0),5)

while True:
    check,img = video.read()  
    success,bbox=tracker.update(img)
    if success:
        drawbox(img,bbox)
    else:
        cv2.putText(img,"LOST",(75,90),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),2) 
    goaltrack(img,bbox)
    cv2.imshow("result",img)
            
    key = cv2.waitKey(25)

    if key == 32:
        print("Stopped!")
        break


video.release()
cv2.destroyALLwindows()



