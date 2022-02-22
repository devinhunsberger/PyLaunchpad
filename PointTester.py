import cv2
Complete = cv2.imread("Velocity2RGB.png")
i = 0
v = 0
c = 0
f = open('VelRGBLog.txt','w')
while(True):
    while i <= 7:
        h = 0
        while h <= 15:
            if h >= 8:
                x = 82 + 45*h
            else:
                x = 20 + 45*h
            y = 20 + 45*i
            #Rather then making circles, replace this with a logger
            #that logs the rgb values and stores into a folder.
            #we'll then make these into our usable color options in our custom
            #animator. Then its getting the the velocity values
            #(Velocity, (r,g,b))
            f.write(str(v) + ' ' + str(Complete[y, x]) + '\n')
            h += 1
            v += 1
        i += 1
    
    cv2.imshow("Final", Complete)
    k = cv2.waitKey(32)
    if k == 32:
        break
cv2.destroyAllWindows()
f.close()
