import tensorflow.keras
import numpy as np
import cv2
import random
from game import mapper, calculate_winner
import time

np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model("keras_model.h5")

#  0_Rock  1_Paper  2_Scissors  3_YourTurn

s = ["images/0.png", "images/1.png", "images/2.png", "images/3.jfif"]

# Setting default cam to webcam and necesseary variables
img = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
firsttime = False
exit = False
you=0
ai=0
while True:
    font = cv2.FONT_HERSHEY_SIMPLEX
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

    start = time.time()
    end = time.time()
    check = 0.0
    
    while(True):
        
        end = time.time()
        check = end-start
        ret, frame = img.read()
        frame = cv2.flip(frame, 1)
        frame = cv2.rectangle(frame, (70, 70), (340, 340), (0, 0, 255), 3)
        cv2.putText(frame,  "------".format(you), (475, 87),font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame,  "You : {}".format(you), (495, 117),font, 1, (0, 0, 0), 2, cv2.LINE_AA)  
        cv2.putText(frame,  "A.I : {}".format(ai), (515, 157),font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame,  "------".format(you), (475, 187),font, 1, (0, 0, 0), 2, cv2.LINE_AA)
        for i in range(112,192,50):
            cv2.putText(frame,  "|".format(you), (475, i),font, 1, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(frame,  "|".format(you), (625, i),font, 1, (0, 0, 0), 2, cv2.LINE_AA)

        if not ret:
            continue

        if(firsttime):
            t = random.choice([0, 1, 2])
            computer_move_name = mapper(t)
            frame = cv2.rectangle(frame, (70, 70), (340, 340), (0, 0, 255), 3)
            frame2 = frame[70:340, 70:340]
            image = cv2.resize(frame2, (224, 224))
            image_array = np.asarray(image)
            normalized = (image_array.astype(np.float32) / 127.0) - 1
            data[0] = normalized

            pred = model.predict(data)
            move_code = np.argmax(pred[0])
            user_move_name = mapper(move_code)
            result = cv2.imread(s[t])
            if(user_move_name == "none"):
                result = cv2.imread(s[3])

            cv2.imshow("img", frame)
            if(check < 4):
                cv2.putText(frame,  "Deliver in {}".format(
                    4-int(check)), (115, 320), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

            elif(check >= 4):
                cv2.imshow("result", result)
                cv2.putText(frame,  "Winner : ", (40, 400),
                            font, 1, (0, 255, 0), 2, cv2.LINE_AA)
                cv2.putText(frame,  winner, (250, 400), font,
                            1, (0, 255, 0), 2, cv2.LINE_AA)
                if user_move_name != "none":
                    result = calculate_winner(user_move_name, computer_move_name)
                    if(result==0):
                        ai=ai+1
                        winner="A.I"
                    else:
                        you=you+1
                        winner="Y.O.U"
                
                firsttime = False

        if(not firsttime):
            cv2.putText(frame,  "Winner : ", (40, 400),
                        font, 1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(frame,  winner, (250, 400), font,
                        1, (0, 255, 0), 2, cv2.LINE_AA)
            cv2.putText(frame,  "Press S to Play", (80, 210),
                        font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("img", frame)
        if cv2.waitKey(1) & 0xff == ord('s'):
            firsttime = True
            start = time.time()
            break

        # To Exit from the game...
        if cv2.waitKey(1) & 0xff == ord('q'):
            exit = True
            break

    result = cv2.imread(s[3])
    if cv2.waitKey(1) & 0xff == ord('q'):
        exit = True
        break
    if(exit):
        break
    cv2.imshow("img", frame)
    cv2.imshow("result", result)


img.release()
cv2.destroyAllWindows()
