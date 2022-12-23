import numpy as np
import cv2

def nothing():
    pass


video_feed = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_DUPLEX
cv2.namedWindow("Trackbars")
cv2.createTrackbar("L-H", "Trackbars", 165, 180, nothing)
cv2.createTrackbar("L-S", "Trackbars", 157, 255, nothing)
cv2.createTrackbar("L-V", "Trackbars", 230, 255, nothing)
cv2.createTrackbar("U-H", "Trackbars", 180, 180, nothing)
cv2.createTrackbar("U-S", "Trackbars", 255, 255, nothing)
cv2.createTrackbar("U-V", "Trackbars", 255, 255, nothing)


while True:
    _, frames = video_feed.read()
    hsv = cv2.cvtColor(frames, cv2.COLOR_BGR2HSV)

    L_H = cv2.getTrackbarPos("L-H", "Trackbars")
    L_S = cv2.getTrackbarPos("L-S", "Trackbars")
    L_V = cv2.getTrackbarPos("L-V", "Trackbars")
    U_H = cv2.getTrackbarPos("U-H", "Trackbars")
    U_S = cv2.getTrackbarPos("U-S", "Trackbars")
    U_V = cv2.getTrackbarPos("U-V", "Trackbars")

    lower_red = np.array([L_H, L_S, L_V])
    upper_red = np.array([U_H, U_S, U_V])

# CREATING A MASK TO HIGHLIGHT THE OBJECT.
    mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.erode(mask, (5, 5))
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for count in contours:
        contour_area = cv2.contourArea(count)

# REDUCING NUMBER OF CONTOURS.
        approx = cv2.approxPolyDP(count, 0.02*cv2.arcLength(count, True), True)
        x = approx.ravel()[0]
        y = approx.ravel()[1]
        if contour_area > 400:
            cv2.drawContours(frames, [approx], 0, (0,  0,  0), 5)

            if 5 < len(approx) < 100:
                cv2.putText(frames, "Arrow", (x, y), font, 1, (0, 0, 0))

    cv2.imshow("Video Feed", frames)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(1)
# PRESS THE Q KEY TO CLOSE ALL THE WINDOWS
    if key == 81:
        break

video_feed.release()
cv2.destroyAllWindows()