import cv2
import os
import numpy as np
from keras_squeezenet import SqueezeNet
from keras.optimizers import Adam
from tensorflow.python.keras.utils import np_utils
from keras.layers import Dropout, GlobalAveragePooling2D, Conv2D, Dense,   MaxPooling2D, Flatten
from keras.models import Sequential


#from keras.layers import Activation, Dropout, Convolution2D, GlobalAveragePooling2D
IMG_SAVE_PATH = 'train_data'

CODES = {
    "rock": 0,
    "paper": 1,
    "scissors": 2,
    "none": 3
}

NUM_CLASSES = len(CODES)


def code_conv(val):
    return CODES[val]


dataset = []
for directory in os.listdir(IMG_SAVE_PATH):
    path = os.path.join(IMG_SAVE_PATH, directory)
    if not os.path.isdir(path):
        continue
    for item in os.listdir(path):

        if item.startswith("."):
            continue
        img = cv2.imread(os.path.join(path, item))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (240, 240))
        dataset.append([img, directory])

data, labels = zip(*dataset)
labels = list(map(code_conv, labels))
labels = np_utils.to_categorical(labels)

'''
model = Sequential([
    SqueezeNet(input_shape=(240, 240, 3), include_top=False),
    Dropout(0.5),
    Convolution2D(NUM_CLASSES, (1, 1), padding='valid'),
    Activation('relu'),
    GlobalAveragePooling2D(),
    Activation('softmax')
])

'''
model = Sequential()
model.add(SqueezeNet(input_shape=(240, 240, 3), include_top=False))
model.add(Dropout(0.4))
model.add(Conv2D(32, (1, 1), padding='valid', activation='relu'))
model.add(GlobalAveragePooling2D())
model.add(Dense(NUM_CLASSES, activation='softmax'))

##############
'''
   model = Sequential()
   model.add(Conv2D(32, kernel_size=(3, 3),
                    activation='relu', input_shape=(240, 240, 3)))
   model.add(Conv2D(64, (3, 3), activation='relu'))
   model.add(MaxPooling2D(pool_size=(2, 2)))
   model.add(Dropout(0.25))
   model.add(Flatten())
   model.add(Dense(128, activation='relu'))
   model.add(Dropout(0.5))
   model.add(Dense(NUM_CLASSES, activation='softmax'))

   '''

print(model.summary())

model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='categorical_crossentropy',  metrics=['accuracy'])

model.fit(np.array(data), np.array(labels), epochs=10, verbose=2)
model.save("RPS-model.h5")
