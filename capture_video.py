import numpy as np
import cv2
import os
import extract_features as ef

def grab_frames(max_count, base_dir):
    cap = cv2.VideoCapture(0)
    count = 0
    frames = []
    while(count < max_count):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        frames.append(gray)
        count += 1
    
    cap.release()
    cv2.destroyAllWindows()
    return frames 


if __name__ == '__main__':
    frames = grab_frames(20, './')
    for i, f in enumerate(frames):
        print("Extracting features from frame {}".format(i))
        descriptors = ef.extract_features(f)
