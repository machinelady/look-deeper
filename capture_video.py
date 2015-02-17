import numpy as np
import cv2
import os

def grab_frames(max_count, base_dir):
    cap = cv2.VideoCapture(0)
    count = 0
    files = []
    while(count < max_count):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        filename = os.path.join(base_dir, 'frame{0}.jpg'.format(count))
        files.append(filename)
        cv2.imwrite(filename, frame)
        count += 1
    
    cap.release()
    cv2.destroyAllWindows()
    return files
