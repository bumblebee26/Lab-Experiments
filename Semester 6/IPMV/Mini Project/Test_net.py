import os
import numpy as np
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
import pandas as pd
from keras import layers, models, optimizers
from keras.models import model_from_json
from sklearn.model_selection import train_test_split
import cv2


TRAIN_DIR = 'C:/Users/Sanjeet/Documents/College/College TE/Cat image classifier/test_set'

def prepare_data(list_of_images):
    x = []
    y = []
    i = 1
    di = os.listdir(TRAIN_DIR)
    file  = "C:/Users/Sanjeet/Documents/College/College TE/Cat image classifier/test_set/"
    for image in di:
        if image.endswith(".jpg"):
            print(i)
            x.append(np.array(cv2.resize(cv2.imread(list_of_images+'/'+image), (224,224), interpolation=cv2.INTER_CUBIC)))
            word_label = image.split('.')[-3]
            if word_label == 'cat':
                b = np.array(0)
                y.append(b)
            elif word_label == 'dog':
                b = np.array(1)
                y.append(b)

            i = i+1
    return x,y

X_test,Y_test = prepare_data(TRAIN_DIR)
print('split')
X_test = np.array(X_test)
Y_test = np.array(Y_test)
print('arrayed')


json_file = open('C:/Users/Sanjeet/Documents/College/College TE/Cat image classifier/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("C:/Users/Sanjeet/Documents/College/College TE/Cat image classifier/model.h5")
print("Loaded model from disk")
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

pred = loaded_model.predict(X_test)
pred = (pred > 0.5)
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, pred)
print(cm)
scores = loaded_model.evaluate(X_test, Y_test,verbose = 0 )
print("\n%s: %.2f%%" % (loaded_model.metrics_names[1], scores[1]*100))
