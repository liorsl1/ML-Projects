import cv2
import numpy as np
frameWidth = 680
frameHeight = 540
cap = cv2.VideoCapture(0)   # 0 is the default webcam, else we need to specify the camera id.

#setting the settings of the video : 3 - is the width id, 4 - is the height id, 10 - is the brightness id.
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)

myColors = [[5,107,160,19,255,255],
            [123,75,0,179,255,255],
            [102,130,0,170,255,164],
            [70,97,51,89,255,255]]

myColorValues = [[13,138,229],  #BGR
                 [229,13,207],
                 [229,48,13],
                 [20,229,13]]

myPoints = [] #[x , y ,colorID]

def findColor(img,myColors,myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints=[]
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        x,y = getCountours(mask)
        cv2.circle(imgResult,(x,y),10,myColorValues[count],cv2.FILLED)
        if x!=0 and y!=0:
            newPoints.append([x,y,count])
        count +=1
    return newPoints        

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult,(point[0],point[1]),9,myColorValues[point[2]],cv2.FILLED)

def getCountours(img):
    x,y,w,h = 0,0,0,0
    contours , hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) #retrievs the outer edges
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area >500: #for some reason the 7th shape has area of 2.5 , while the others have more than 1000
            peri = cv2.arcLength(cnt,True)
            #approximate how many corners points :
            approx = cv2.approxPolyDP(cnt, 0.02*peri,True)
            if(len(approx)<8):
                cv2.drawContours(imgResult, cnt, -1, (255,0,0),1)
            
            # getting a bounding box properties from the corners approx
            x,y,w,h = cv2.boundingRect(approx)
            
    return x+w//2,y

# Our identification method of the optimized color values :

# def TrackBar_changed(a):
#     pass

# cv2.namedWindow("TrackBars")
# cv2.resizeWindow("TrackBars",640,240)
# cv2.createTrackbar("Hue Min","TrackBars",5,179,TrackBar_changed)
# cv2.createTrackbar("Hue Max","TrackBars",19,179,TrackBar_changed)
# cv2.createTrackbar("Sat Min","TrackBars",107,255,TrackBar_changed)
# cv2.createTrackbar("Sat Max","TrackBars",255,255,TrackBar_changed)
# cv2.createTrackbar("Val Min","TrackBars",10,255,TrackBar_changed)
# cv2.createTrackbar("Val Max","TrackBars",255,255,TrackBar_changed)

# while True:
#     _, img = cap.read()
#     imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h_min=cv2.getTrackbarPos("Hue Min","TrackBars")
#     h_max=cv2.getTrackbarPos("Hue Max","TrackBars")
#     s_min=cv2.getTrackbarPos("Sat Min","TrackBars")
#     s_max=cv2.getTrackbarPos("Sat Max","TrackBars")
#     v_min=cv2.getTrackbarPos("Val Min","TrackBars")
#     v_max=cv2.getTrackbarPos("Val Max","TrackBars")
#     #create a mask according to the trackbar values :
#     lower = np.array([h_min,s_min,v_min])
#     upper = np.array([h_max,s_max,v_max])
#     mask = cv2.inRange(imgHSV,lower,upper)

#     cv2.imshow("orig",img)
# # we found our optimized colors, lets get the colors out of it :
#     if cv2.waitKey(1) & 0xFF == ord('r'):
#         mask = cv2.bitwise_and(img,img,mask=mask)
#         print(h_min,h_max,s_min,s_max,v_min,v_max)
#         break
#     cv2.imshow("masked",mask)
#     cv2.waitKey(1)
# cv2.imshow("masked",mask)
# cv2.waitKey(1)
    
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img,myColors,myColorValues)
    if len(newPoints)!=0:
        for newpoint in newPoints:
            myPoints.append(newpoint)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints,myColorValues)

    cv2.imshow("live feed",imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):   #somekind of mask with the key (the mask is AND 0xFF)
        break