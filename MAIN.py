import cv2
import numpy as np
import tracking
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
from scipy import ndimage
#im adding a comment and a random variable

q=1

h = 0
h1 = 400
w = 0
w1 = 300
angle = 0.8#transformation to get correct alignment
filter = 10

length = 2.0#mm
breadth = 0.1#mm
height = 0.1#mm
volume = (length*breadth*height)*0.001
concen = 0

























particle_centers = []#from current frame
particle_id = []#labels from current frame

cap = cv2.VideoCapture("")

_,frame = cap.read()
frame = frame[0:h1, 0:w1]
frame = ndimage.rotate(frame, angle)

frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

averageValue1 = np.float32(frame)


while True:
    particle_centers = []  # from current frame
    particle_id = []  # labels from current frame
    _,frame = cap.read()
    frame1 = frame[0:h1, 0:w1]
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
                    i = i+1;

        if i != 0:
            resulttrack = tracking.neighbours(particle_centers)
            concen = concen+tracking.concentration(particle_centers,volume)

                #if resulttrack:
                 #   print("result is : ",resulttrack)
    cv2.line(frame1, (filter, 0), (filter, 400), (255, 255, 0), thickness=1)



    cv2.imshow('result of difference', frame1)

    k = cv2.waitKey(1) & 0xff
    if k == 27:
        break






cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

fig = plt.figure(figsize=(10, 7))
bins=range(0, 300+5 + 5, 5)

mean = np.mean(resulttrack)
print("mean is :",mean)

plt.hist(resulttrack, bins, alpha=0.5, label='x',density=True)

plt.legend(loc='upper right')
plt.show()


plt.title("Numpy Histogram")























