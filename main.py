import tensorflow.keras
import numpy as np
import cv2
import random
from game import mapper, calculate_winner

np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model("keras_model.h5")

#  0_Rock  1_Paper  2_Scissors  3_YourTurn

s = ["0.jfif", "1.jfif", "2.png", "3.jfif"]

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

    # pre = model.predict(data)
    
    pred = model.predict(data)
    #print(pred)
    move_code = np.argmax(pred[0])
    t = random.choice([0, 1, 2])


    user_move_name = mapper(move_code)

    
    result = cv2.imread(s[t])

    # predict the winner (human vs computer)
    if prev_move != user_move_name:
        if user_move_name != "none":
            computer_move_name = t
            winner = calculate_winner(user_move_name, computer_move_name)
        else:
            computer_move_name = "none"
            winner = "Waiting..."
    prev_move = user_move_name

    font = cv2.FONT_HERSHEY_SIMPLEX
    #cv2.putText(frame, "Winner: " + winner, (80, 440), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

# the above line is commented bcoz it produces some error

    cv2.imshow("img", frame)
    cv2.imshow("result", result)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
