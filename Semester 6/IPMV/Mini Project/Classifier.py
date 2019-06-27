from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
import os, cv2, re, random
import numpy as np
import pandas as pd
from keras import layers, models, optimizers
from keras.models import model_from_json
print('start')


json_file = open('C:/Users/Sanjeet/Documents/College/College TE/Cat image classifier/model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)

loaded_model.load_weights("C:/Users/Sanjeet/Documents/College/College TE/Cat image classifier/model.h5")
print("Loaded model from disk")


image = input()
y = []
x = np.array(cv2.resize(cv2.imread('C:/Users/Sanjeet/Documents/College/College TE/Cat image classifier/'+image), (224,224), interpolation=cv2.INTER_CUBIC))
x = x.reshape([-1,224,224,3])



loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
# pred = model.predict(X_test)
# pred = (pred > 0.5)
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(Y_test, pred)


pred = loaded_model.predict(x)
# pred = (pred > 0.5)
# print(pred)
# if pred<=0.6:
#     print('cat')
# else:
#     print('dog')
print(pred)
