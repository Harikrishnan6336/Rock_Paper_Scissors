import tensorflow.keras
import numpy as np
import cv2
import time
np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model("keras_model.h5")


s = ["images/0.jfif", "images/1.jfif", "images/2.png","images/3.jfif"]

img = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
start=time.time()
end=time.time()
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
    end=time.time()
    pre = model.predict(data)
    result = cv2.imread(s[np.argmax(pre[0])])
    cv2.imshow("img", frame)
    if(end-start<6):
        cv2.putText(frame, "Deliver in", (160, 30),
			cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        print(end-start)
        if(end-start<2):
            cv2.putText(frame, "3", (160, 60),
			    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        elif(end-start<4):
            cv2.putText(frame, "2", (160, 60),
			    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        else:
            cv2.putText(frame, "1", (160, 60),
			    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        continue
    else :
        cv2.imshow("result", result)
        start=end
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
