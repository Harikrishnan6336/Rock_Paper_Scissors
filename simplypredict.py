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
check=0
while True:
    end=time.time()
    ret, frame = img.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        continue

    frame = cv2.rectangle(frame, (360, 100), (610, 350), (0, 0, 255), 3)
    frame2 = frame[360:610, 100:350]
    check=5-end+start
    cv2.putText(frame, "Deliver within {}".format(int(check)), (200, 30),
		cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
    image = cv2.resize(frame2, (224, 224))
    image_array = np.asarray(image)
    normalized = (image_array.astype(np.float32) / 127.0) - 1
    data[0] = normalized
    print(end-start)
    cv2.imshow("img", frame)  
    pre = model.predict(data)
    result = cv2.imread(s[np.argmax(pre[0])])
    if(end-start>4):
        start=end 
        cv2.imshow("result", result)
        time.sleep(1.0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
          
    