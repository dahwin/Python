import cv2
import mediapipe as mp
import pyautogui
camera = cv2.VideoCapture(1)
face_mash = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w , screen_h  = pyautogui.size()
while True:
    _, frame = camera.read()
    frame = cv2.flip(frame,1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mash.process(rgb_frame)
    landmark_point = output.multi_face_landmarks
    frame_h , frame_w , _ = frame.shape
    if landmark_point:
        landmarks = landmark_point[0].landmark
        for id ,landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x , y) , 3, (0 , 255, 0))
            if id == 1:
                screen_x = screen_w / frame_w * x
                screen_y = screen_h / frame_h * y
                pyautogui.moveTo(x , y)
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))
        print(left[0].y, left[1].y)
    cv2.imshow('eye controlled mouse', frame)
    cv2.waitKey(1)