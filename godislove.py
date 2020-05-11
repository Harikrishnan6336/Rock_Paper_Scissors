import tensorflow.keras
import numpy as np
import cv2
import random
from game import mapper, calculate_winner
import time
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model("keras_model.h5")

#  0_Rock  1_Paper  2_Scissors  3_YourTurn

s = ["images/0.jfif", "images/1.jfif", "images/2.png", "images/3.jfif"]

img = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
prev_move = None

while True:
    ret, frame = img.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        continue

    frame = cv2.rectangle(frame, (70, 70), (340, 340), (0, 0, 255), 3)
    frame2 = frame[70:340, 70:340]
    image = cv2.resize(frame2, (224, 224))
    image_array = np.asarray(image)
    normalized = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized


    winner = "None"

    result = cv2.imread(s[3])
    pred = model.predict(data)
    move_code = np.argmax(pred[0])
    inp = move_code
    #print(move_code)
    firsttime = 1
    start=time.time()
    end=time.time()
    check=0.0
    while(move_code == inp and move_code != 3):
        end=time.time()
        check=end-start
        ret, frame = img.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.rectangle(frame, (70, 70), (340, 340), (0, 0, 255), 3)
        if not ret:
            continue
        if(firsttime == 1):
            t = random.choice([0, 1, 2])
            computer_move_name = mapper(t)
            print("kk")
            #frame = cv2.rectangle(frame, (70, 70), (340, 340), (0, 0, 255), 3)
            frame2 = frame[70:340, 70:340]
            image = cv2.resize(frame2, (224, 224))
            image_array = np.asarray(image)
            normalized = (image_array.astype(np.float32) / 127.0) - 1
            data[0] = normalized

            pred = model.predict(data)
            move_code = np.argmax(pred[0])
            user_move_name = mapper(move_code)
            result = cv2.imread(s[t])

            if user_move_name != "none":
                #computer_move_name = t
                winner = calculate_winner(user_move_name, computer_move_name)
       
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,  "Winner : ", (40, 440), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            cv2.putText(frame,  winner, (250, 440), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
            
            cv2.imshow("img", frame)
            if(check<4):
                cv2.putText(frame,  "Deliver in {}".format(4-int(check)) , (40, 350), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
            elif(check>=4):
                cv2.imshow("result", result)
                firsttime = 0

        cv2.putText(frame,  "Winner : ", (40, 400), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame,  winner, (250, 400), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
        if(firsttime == 0):
            cv2.putText(frame,  "Press 's' to continue...", (250, 450), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("img", frame)   
        if cv2.waitKey(1) & 0xff == ord('s'):
            start=time.time()
            break

    result = cv2.imread(s[3])
    cv2.imshow("img", frame)
    cv2.imshow("result", result)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break