import cv2
import numpy as np
import tracking
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from scipy import ndimage


h = 200
h1 = 1000
w = 0
w1 = 300
angle = -89.1#transformation to get correct alignment
filter = 115
p1 = 146
p2 = 165
d = p2-p1
channel_width = 100#microns


particle_centers = []#from current frame
particle_id = []#labels from current frame

cap = cv2.VideoCapture("C:\\Users\\vraja\\PycharmProjects\\BD_PROJECT\data\\117to702ul_min_beadtosheath\\afterexpansion.avi")

_,frame = cap.read()
frame = frame#[0:h1, 0:w1]
frame = ndimage.rotate(frame, angle)

frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

averageValue1 = np.float32(frame)




while True:
    particle_centers = []  # from current frame
    particle_id = []  # labels from current frame
    _,frame = cap.read()
    frame1 = frame#[0:h1, 0:w1]
    frame1 = ndimage.rotate(frame1, angle)

    frame1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)

    cv2.accumulateWeighted(frame1, averageValue1, 0.05)

    resultavg = cv2.convertScaleAbs(averageValue1)

    result = cv2.absdiff(frame1,resultavg, None)
    ret, result = cv2.threshold(result, 5, 255, 0)
    contours, heirarchy = cv2.findContours(result,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    i=0;

    if len(contours) != 0:

        for c in contours:#check through contours
            if cv2.contourArea(c)>2:#select only contours larger than this
                #cv2.drawContours(frame, c, -1, (255, 0, 0), 1)
                x, y, w, h = cv2.boundingRect(c)
                if x>filter:
                    particle_centers.append([y])

                    particle_id.append(i)
                    cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 255, 0), 1)
                    i = i+1

        if i > 1:
            resulttrack = tracking.neighbours(particle_centers)
            #print(i)
            #print(resulttrack)

                #if resulttrack:
                 #   print("result is : ",resulttrack)
    cv2.line(frame1, (filter, 0), (filter, 400), (255, 255, 0), thickness=1)
    cv2.line(frame1, (p1, 100), (p2, 100), (255, 255, 0), thickness=1)

    cv2.imshow('result of difference', frame1)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break






cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()



[float(i) for i in resulttrack]
resultf= [i *(channel_width/d) for i in resulttrack]


fig = plt.figure(figsize=(10, 7))
bins=range(0, 1000 + 50, 50)

mean = np.mean(resultf)
std = np.std(resultf)
print("result is:",resultf)
print("mean in um :",mean)
print("std in um :",std)


plt.hist(resultf, bins, alpha=0.5, label='spacing distribution',density=True,cumulative=True)
plt.xlabel('Spacing (um)')
plt.ylabel('Relative frequency')
plt.legend(loc='upper right')
plt.show()
plt.title("Spacing Distribution")























