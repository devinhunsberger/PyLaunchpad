import mido
import cv2

#Color library using dictionary from RGB to velocity value of the Launchpad MK2
from ClearLaunchpad import RemoveNotes, ClearScreen
from FirstMido import FillNotes

cap = cv2.imread("Velocity2RGB.png")
Complete = cap.copy()
while(True):
    Mat = cv2.inRange(cap, (0, 0, 0), (254, 254, 254))
    cv2.imshow("Mat", Mat)
    contours, hierarchy = cv2.findContours(Mat, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for i, c in enumerate(contours):
        if hierarchy[0][i][2] == -1 or hierarchy[0][i][2] > 1:
            if cv2.contourArea(c) < 60000 and cv2.contourArea(c) > 1000:
                try:
                    cX = int(cv2.moments(c)["m10"] / cv2.moments(c)["m00"])
                except ZeroDivisionError:
                     cX = 0
                try:
                     cY = int(cv2.moments(c)["m01"] / cv2.moments(c)["m00"])
                except ZeroDivisionError:
                     cY = 0
                points = cv2.circle(Complete, (cX, cY), 0, (255,255,255), -1)
                print(cX,cY)
    cv2.imshow("Final", Complete)
    k = cv2.waitKey(32)
    if k == 32:
        break
cap.release()
cv2.destroyAllWindows()


#Each center on the x axis is spaced out by 45 units, starting with 20 as the first center point (Left to right). min of 20 max of 335
#As for y 21 and also moves by 45 units (we can go with 20 and it will still be the same). min of 20 max of 756
