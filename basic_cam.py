import cv2, time

video = cv2.VideoCapture(0)

a = 0

while True:
    a=a+1
    check, frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2Luv)
    #time.sleep3
    cv2.imshow("Capturing",gray)

    key = cv2.waitKey(1)
    print(gray)

    if key==ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows