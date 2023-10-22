import cv2
video = cv2.VideoCapture('fakelove.mp4')
while True:
    _ , frame = video.read()
    cv2.imshow('windows', frame)
    cv2.waitKey(2)