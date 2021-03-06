import os
import cv2
import numpy as np
import time

cap = cv2.VideoCapture(0)

file_index = 0

if not os.path.exists("calibration_data/calibration_frames/"):
    os.makedirs("calibration_data/calibration_frames/")

while True:

    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow("frame", frame)
    key = cv2.waitKey(100) & 0xFF

    if key == ord("q"):
        break

    if key == ord("s"):
        filename = "calibration_data/calibration_frames/frame_" + str(file_index) + str(time.time()) + ".png"
        cv2.imwrite(filename, frame)
        file_index += 1

# When everything done, release the capture
cv2.destroyAllWindows()
