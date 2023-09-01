import cv2

webcam = cv2.VideoCapture(0)

while True:
    ret, frame = webcam.read() #ret is a boolean, says whether your camera is returning an image

    if ret == True:
        cv2.imshow('picture', frame)
        key = cv2.waitKey(1000)
        if key == ord("q"):
            break

webcam.release()
cv2.destroyAllWindows()
