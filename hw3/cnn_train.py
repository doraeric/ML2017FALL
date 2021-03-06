#!/usr/bin/env python3
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dropout
from keras.layers import ZeroPadding2D, BatchNormalization
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, History, EarlyStopping

class DataSet:
    def __init__(self, inputs):
        self.inputs = inputs
    def shuffle():
        permutation = np.random.permutation(self.inputs.shape[0])
        self.inputs = self.inputs[permutation]
        self.labels = self.labels[permutation]

def load_data():
    npz = np.load('input_data/train.npz')
    data = DataSet(npz['inputs'])
    data.labels = npz['labels']
    return data

def default_train(model, dataSet, epochs=3, optimizer = Adam()):
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    history = History()
    # checkpointer = ModelCheckpoint(filepath='weighs.h5', monitor='val_loss', verbose=1, save_best_only=True)
    checkpointer = ModelCheckpoint(filepath='weighs.h5', monitor='val_acc', verbose=1, save_best_only=True)
    earlystopping = EarlyStopping(monitor='val_acc', patience=20)
    # plot
    from keras.callbacks import TensorBoard
    tbCallBack = TensorBoard(log_dir='./Graph', histogram_freq=0, write_graph=True, write_images=True)
    model.fit(dataSet.inputs, dataSet.labels, batch_size=128, epochs=epochs, validation_split=0.3, callbacks=[history, checkpointer, earlystopping, tbCallBack])
    # end
    # model.fit(dataSet.inputs, dataSet.labels, batch_size=128, epochs=epochs, validation_split=0.3, callbacks=[history, checkpointer, earlystopping])
    return history

def my_model(dataSet):
    # CNN
    model = Sequential()
    model.add(Conv2D(filters=25, kernel_size=(3, 3), input_shape=(48, 48, 1)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=50, kernel_size=(3, 3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=50, kernel_size=(3, 3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Conv2D(filters=50, kernel_size=(3, 3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    # Fully connected
    model.add(Dense(300, activation='relu'))
    model.add(Dense(300, activation='relu'))
    model.add(Dense(300, activation='relu'))
    model.add(Dropout(0.3))
    model.add(Dense(7, activation='softmax'))
    return model

def DNN():
        model = Sequential()
        model.add(Dense(1024, activation='relu', input_shape=(48* 48,)))
        model.add(Dense(1024, activation='relu'))
        model.add(Dense(756, activation='relu'))
        model.add(Dropout(0.3))
        model.add(Dense(7, activation='softmax'))
        return model

def VGG16():
    model = Sequential()
    model.add(ZeroPadding2D((1,1),input_shape=(48, 48, 1)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(256, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(256, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(256, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(512, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(512, (3, 3), activation='relu'))
    model.add(ZeroPadding2D((1,1)))
    model.add(Conv2D(512, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2,2), strides=(2,2)))

    model.add(Flatten())
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(4096, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(7, activation='softmax'))
    return model

def AlexNet():
    model = Sequential()
    model.add(Conv2D(64, (3, 3), input_shape=(48, 48, 1)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D((2,2))) # 23
    model.add(Dropout(0.5))
    model.add(Conv2D(128, (2, 2)))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D((2,2))) # 11
    model.add(Dropout(0.5))
    model.add(Conv2D(192, (2, 2), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Conv2D(192, (2, 2), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Conv2D(192, (2, 2))) # 7
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(MaxPooling2D((2,2)))
    model.add(Dropout(0.5))

    model.add(Flatten())
    model.add(Dense(1024))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(512))
    model.add(BatchNormalization())
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    model.add(Dense(7))
    model.add(BatchNormalization())
    model.add(Activation('softmax'))
    return model

def main():
    face = load_data()

    model = AlexNet()
    hist = default_train(model, face)
    h = hist.history

#     import matplotlib
#     matplotlib.use('agg')
#     import matplotlib.pyplot as plt
#     fig, ax = plt.subplots()
#     ax.plot(range(50), h['acc'], label='train')
#     ax.plot(range(50), h['val_acc'], label='valid')
#     ax.legend()
#     ax.set_xlabel('# of epoch')
#     ax.set_ylabel('Accuracy')
#     ax.set_axisbelow(True)
#     ax.yaxis.grid(color='gray', linewidth=0.3)
#     ax.xaxis.grid(color='gray', linewidth=0.3)
#     fig.savefig('fig.png')
#     fig.savefig('output/train50-2.png')

if __name__ == '__main__':
    main()
