import cv2
video = cv2.VideoCapture(0)

while True:
    ret, img = video.read()
    print(img)
    cv2.imshow("Image", img)
    k = cv2.waitKey()
    if k == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

