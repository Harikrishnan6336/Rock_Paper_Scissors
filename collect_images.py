import os
import sys
import cv2

desc = '''

Error:  collect_images.py missing 2 required positional arguments

Usage: python collect_images.py <label_name> <num_samples>

The label_name should be 'rock', 'paper', 'scissors' and 'none'
The script will collect <num_samples> number of images and store them
in its own directory.

Minimum 100 images should be provided.

The image to be captured must be strictly inside the rectangle.

Press 'c' to start/pause the image collecting process.
Press 'q' to quit.

'''

try:
    label_name = sys.argv[1]
    num_samples = int(sys.argv[2])

except:
    print(desc)
    exit(-1)

if num_samples < 100:
    print("\n Please, provide minimum 100 images to train. ")
    exit(-1)
IMG_SAVE_PATH = 'train_data'
IMG_CLASS_PATH = os.path.join(IMG_SAVE_PATH, label_name)

try:
    os.mkdir(IMG_SAVE_PATH)
except FileExistsError:
    pass
try:
    os.mkdir(IMG_CLASS_PATH)
except FileExistsError:
    print("{} directory already exists.".format(IMG_CLASS_PATH))
    print("All images gathered will be saved along with existing items in this folder")

cap = cv2.VideoCapture(0)

start = False
count = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    if not ret:
        continue

    if count == num_samples:
        break

    cv2.rectangle(frame, (320, 100), (570, 350), (0, 0, 255), 2)

    if start:
        roi = frame[100:350, 320:570]
        save_path = os.path.join(IMG_CLASS_PATH, '{}.jpg'.format(count + 1))
        cv2.imwrite(save_path, roi)
        count += 1

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Collecting {}".format(count),
                (5, 50), font, 0.7, (0, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Press 'c' to start/pause the image collection process",
                (25, 410), font, 0.7, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Collecting images", frame)

    k = cv2.waitKey(10)
    if k == ord('c'):
        start = not start

    if k == ord('q'):
        break

print("\n{} image(s) saved to {}".format(count, IMG_CLASS_PATH))
cap.release()
cv2.destroyAllWindows()
