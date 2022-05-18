import cv2
import mediapipe as mp
import numpy as np
import time
import array as arr

#creating variables from imported libaries
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

#calculate angles
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

#countdown
def countdown(Time):
    while Time:
        mins,sec=divmod(Time,60)
        timer = '{:02d}:{:02d}'.format(mins,sec)
        print(timer,end="\r")
        time.sleep(1)
        Time-=1

#video
cap = cv2.VideoCapture(0)

#variables
count=0
Time_Fa=0
Time_F=0
Time_L=0
counter =0
stage = None
lapse = 0
i=0
cont=0
Arr=arr.array('i',[])
## Setup mediapipe instance
Time=int(input("Enter amount of time in secs: "))
start=time.time()
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while True:
        ret, frame = cap.read()

        # Recolor image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Make detection
        results = pose.process(image)

        # Recolor back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates
            shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,
                   landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,
                    landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,
                     landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]

            # Calculate angle
            angle = calculate_angle(shoulder, elbow, wrist)

            # Visualize angle
            cv2.putText(image, str(angle),
                        tuple(np.multiply(elbow, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA
                        )
            # timer
            if angle < 160:
                cv2.putText(image, f'FAIL', (170, 280), cv2.FONT_HERSHEY_PLAIN, 10, (0, 0, 255), 10)
                if counter == 0:
                    Start_F=time.time()
                    count=counter
                    counter+=1
                End_F=time.time()
                Time_F=End_F-Start_F
                print("Start_F = ",Start_F)
                print("End_F = ",End_F)
                print("Time_F = ",Time_F)
                cont=0
            else:
                if cont==0:
                    Time_Fa=Time_Fa+Time_F
                    cont+=1
                Curent=time.time()-start
                print("Curent = ",Curent)
                Time_L=Time-Curent+Time_Fa
                print("Time_L",Time_L)
                counter=0
            cv2.putText(image, f'Time left: {int(Time_L)}', (20, 450), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 5)
            if Time_L<0:
                break
        except:
            if Time_L<0:
                break
            else:
                pass

        # Render detections
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245, 117, 66), thickness=2, circle_radius=2),
                                  mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2)
                                  )

        cv2.imshow('Mediapipe Feed', image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()