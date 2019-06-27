from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout, Flatten, Conv2D, MaxPooling2D
import numpy as np
import os, cv2, re, random
import numpy as np
import pandas as pd
from keras import layers, models, optimizers
from sklearn.model_selection import train_test_split
from keras.models import model_from_json
from keras.callbacks import LearningRateScheduler
import math
print('start')

TRAIN_DIR = 'C:/Users/Sanjeet/Documents/College/College TE/Cat image classifier/training_set'
print('images taken')


def prepare_data(list_of_images):
    x = []
    y = []
    i = 1
    di = os.listdir(TRAIN_DIR)
    file  = "C:/Users/Sanjeet/Documents/College/College TE/Cat image classifier/training_set/"
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

X,Y = prepare_data(TRAIN_DIR)
X_train, X_test, Y_train, Y_test= train_test_split(X,Y, test_size=0.2)
print('split')
X_train = np.array(X_train)
X_test = np.array(X_test)
Y_train = np.array(Y_train)
Y_test = np.array(Y_test)
print('arrayed')


model = Sequential()

# 1st Convolutional Layer
model.add(Conv2D(filters=96, input_shape=(224,224,3), kernel_size=(11,11), strides=(4,4), padding='valid'))
model.add(Activation('relu'))
# Max Pooling
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))

# 2nd Convolutional Layer
model.add(Conv2D(filters=256, kernel_size=(11,11), strides=(1,1), padding='valid'))
model.add(Activation('relu'))
# Max Pooling
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))

# 3rd Convolutional Layer
model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))
model.add(Activation('relu'))

# 4th Convolutional Layer
model.add(Conv2D(filters=384, kernel_size=(3,3), strides=(1,1), padding='valid'))
model.add(Activation('relu'))

# 5th Convolutional Layer
model.add(Conv2D(filters=256, kernel_size=(3,3), strides=(1,1), padding='valid'))
model.add(Activation('relu'))
# Max Pooling
model.add(MaxPooling2D(pool_size=(2,2), strides=(2,2), padding='valid'))

# Passing it to a Fully Connected layer
model.add(Flatten())
# 1st Fully Connected Layer
model.add(Dense(4096, input_shape=(224*224*3,)))
model.add(Activation('relu'))
# Add Dropout to prevent overfitting
model.add(Dropout(0.4))

# 2nd Fully Connected Layer
model.add(Dense(4096))
model.add(Activation('relu'))
# Add Dropout
model.add(Dropout(0.4))

# 3rd Fully Connected Layer
model.add(Dense(1000))
model.add(Activation('relu'))
# Add Dropout
model.add(Dropout(0.4))

# Output Layer
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.summary()

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

def exp_decay(epoch):
   initial_lrate = 0.0001
   t = epoch
   k = 0.1
   lrate = initial_lrate * math.exp(-k*t)
   print(lrate)
   return lrate
lrate = LearningRateScheduler(exp_decay)
#compile the model
model.fit(X_train, Y_train, batch_size=128, epochs=10,callbacks=[lrate])

scores = model.evaluate(X_train, Y_train,verbose = 0 )
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

# for layer in model.layers:
#     weights = layer.get_weights()

# pred = model.predict(X_test)
# pred = (pred > 0.5)
# from sklearn.metrics import confusion_matrix
# cm = confusion_matrix(Y_test, pred)


model_json = model.to_json()
with open("C:\\Users\\Sanjeet\\Documents\\College\\Audio Processing\\Accent project\\model.json", "w") as json_file:
    json_file.write(model_json)
model.save_weights("C:\\Users\\Sanjeet\\Documents\\College\\Audio Processing\\Accent project\\model.h5")
print("Saved model to disk")

# # load json and create model
# json_file = open('model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# loaded_model = model_from_json(loaded_model_json)
# # load weights into new model
# loaded_model.load_weights("model.h5")
# print("Loaded model from disk")
#
# # evaluate loaded model on test data
# loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
# score = loaded_model.evaluate(X, Y, verbose=0)
# print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1] * 100))