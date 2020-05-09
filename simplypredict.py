import tensorflow.keras
import numpy as np
import cv2

np.set_printoptions(suppress=True)
model = tensorflow.keras.models.load_model("keras_model.h5")


s = ["2.png", "1.jfif", "0.jfif","3.jfif"]

img = cv2.VideoCapture(0)
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

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

    pre = model.predict(data)
    result = cv2.imread(s[np.argmax(pre[0])])

    cv2.imshow("img", frame)
    cv2.imshow("result", result)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
