import cv2
import time

def extract_features(frame):
    sift = cv2.SIFT(contrastThreshold=0.03, sigma=1.0)
    kp, descriptors = sift.detectAndCompute(frame, None)
    
    img=cv2.drawKeypoints(frame,kp,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imwrite('sift_keypoints.jpg',img)
    cv2.imshow("keypoints", img)

    time.sleep(6)
    return descriptors
