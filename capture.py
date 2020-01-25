import argparse

import cv2 
import numpy as np
import os
os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

parser = argparse.ArgumentParser()
parser.add_argument("url", help="The IP your phone is broadcasting to")


def main(url):
    cap = cv2.VideoCapture(url, cv2.CAP_FFMPEG)
    while(True):
        ret, frame = cap.read()
        if frame is not None:
            cv2.imshow('frame', frame)
        q = cv2.waitKey(1)
        if q == ord("q"):
            break
    cv2.destroyAllWindows()

if __name__ == '__main__':
    args = parser.parse_args()
    main(args.url)