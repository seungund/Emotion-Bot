#모델 학습시킨 코드

from tensorflow import keras
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense,Dropout,Flatten
from keras.layers import Conv2D,MaxPooling2D
import os
from matplotlib import pyplot as plt
import numpy as np
from keras.utils import to_categorical

IMG_HEIGHT=48
IMG_WIDTH = 48
batch_size=32

train_path = '/content/drive/MyDrive/emotion-model/shuffled_data(train).csv'
test_path = '/content/drive/MyDrive/emotion-model/shuffled_data(test).csv'
train_data = pd.read_csv(train_path, dtype=int, encoding='CP949')
test_data = pd.read_csv(test_path, dtype=int, encoding='CP949')

class_labels=['Angry', 'Fear', 'Happy','Neutral','Sad','Surprise']

# 'label' 열을 제외한 모든 열을 NumPy 배열로 변환
train_input = train_data.drop('label', axis=1).values

# 'label' 열을 NumPy 배열로 변환
train_target = train_data['label'].values

# 'label' 열을 제외한 모든 열을 NumPy 배열로 변환
test_input = test_data.drop('label', axis=1).values

# 'label' 열을 NumPy 배열로 변환
test_target = test_data['label'].values

train_scaled = train_input / 255.0
test_scaled = test_input / 255.0
print(train_scaled.shape, test_scaled.shape, train_target.shape)

model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1)))

model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Conv2D(256, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.1))

model.add(Flatten())
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(6, activation='softmax'))

model.compile(optimizer = 'adam', loss='categorical_crossentropy', metrics=['accuracy'])
print(model.summary())

train_scaled = train_scaled.reshape(-1, 48, 48, 1)

train_target = to_categorical(train_target, num_classes=6)

history=model.fit(train_scaled,train_target,epochs=25,batch_size=32,)

test_scaled = test_scaled.reshape(-1, 48, 48, 1)

test_target = to_categorical(test_target, num_classes=6)

model.evaluate(test_scaled, test_target)

model.save('emotion_detection_model_15epochs.h5')