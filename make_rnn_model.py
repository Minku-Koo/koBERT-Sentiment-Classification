
# 학습 데이터를 통해 RNN 딥러닝 모델 생성
# build RNN model from train data
# 21.06.29

import json
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2'

import numpy as np
from tensorflow.keras import models, layers, optimizers, losses, metrics
import tensorflow as tf
from keras.preprocessing.sequence import pad_sequences
import csv
import pandas as pd

from tensorflow.keras.layers import Dense, Embedding, Flatten, Dropout
from tensorflow.keras import Input, Model, regularizers

from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers.experimental.preprocessing import TextVectorization
import matplotlib.pyplot as plt

def showModelTrain(history):
    # 6 훈련 과정 시각화 (정확도)
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('Model accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()

    # 7 훈련 과정 시각화 (손실)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()

#   csv 파일 읽어서 x y 리스트 저장
# read csv and make list
x, y = [],[]
path = "./train-data/humanInspection/"
filename = "dataset.tsv" # train data 



with open(path +filename, "rt", encoding="utf-8") as f:
    for l in f.readlines():
        line = l.strip("\n")
        data, value = line.split("\t")
        value = float(value)

        x.append(data)
        y.append(value)

filename2 = "naver-ratings.csv"
x2, y2 = [],[]
f = open(path +filename2, 'rt', encoding='utf-8') #
read = csv.reader(f)
for line in read:
    emotion = float(line[-1])
    y2.append(emotion)
    x2.append(line[0])
    
f.close()


test_percent = 0.3 # test data percent
# make train and test data usin train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_percent)

a,b,c,d =  train_test_split(x2, y2, test_size=test_percent)
x_train += a
x_test += b
y_train += c
y_test += d


def build_model(train_data): # to make rnn model
    train_data = tf.data.Dataset.from_tensor_slices(train_data)
    model = Sequential()
    model.add(Input(shape=(1,), dtype="string")) # input one string data (comment)
    max_tokens = 100000 # dictionary size
    max_len = 64 # comment to vectorize size
    vectorize_layer = TextVectorization( # make textvectorization 
      max_tokens=max_tokens,
      output_mode="int",
      output_sequence_length=max_len,
    )
    dropout_val = 0.4
    vectorize_layer.adapt(train_data.batch(64))
    model.add(vectorize_layer)
    model.add(layers.Embedding(max_tokens + 1, output_dim= 200))
    model.add(Flatten())
    model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    # model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    
    model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    # model.add(Dense(32, activation="relu"))
    # model.add(Dropout(dropout_val))
    # model.add(Dense(32, activation="relu"))
    # model.add(Dropout(dropout_val))
    
    # model.add(Dropout(dropout_val))
    # model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    # model.add(Dropout(dropout_val))
    # model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    # model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    # model.add(Dropout(dropout_val))
    # model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    # model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    # model.add(Dropout(dropout_val))
    # model.add(Dense(32, activation="relu", kernel_regularizer= regularizers.l2(0.001)))
    model.add(Dense(8, activation="relu"))
    model.add(Dense(1, activation="sigmoid"))
    return model

rnn_model =build_model(x_train)
rnn_model.compile( # rnn model compile
        optimizer=  "adam",
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

# model training
history = rnn_model.fit(x_train, y_train, 
                   epochs = 3,  
                   batch_size = 64 , 
                   validation_data = (x_test, y_test) 
                   )
rnn_model.summary()
showModelTrain(history)


model_save_path = "./tf_model/" # model save path
model_name ="rnn-model" #model save file name
tf.saved_model.save(rnn_model, model_save_path+model_name)


'''
 loss: 0.1593 - accuracy: 0.9512 - val_loss: 0.4939 - val_accuracy: 0.8301

'''
