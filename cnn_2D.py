from keras import backend as K
from keras.models import Sequential
from keras.layers import Dense, Conv2D, GlobalAveragePooling2D

def r2(y_true, y_pred):
    SS_res =  K.sum(K.square( y_true-y_pred ))
    SS_tot = K.sum(K.square( y_true - K.mean(y_true) ) )
    return ( 1 - SS_res/SS_tot )

def CNN(synergy):
    # if synergy==True the noisy expectation values are used as input to the CNN.
    model = Sequential()
    if synergy:
        model.add(Conv2D(filters=128, activation = 'relu', kernel_size=3, strides=1, padding='same',
                        input_shape=(None, None, 3)))
    else:
        model.add(Conv2D(filters=128, activation = 'relu', kernel_size=3, strides=1, padding='same',
                        input_shape=(None, None, 2)))
    model.add(Conv2D(filters=128, activation = 'relu', kernel_size=3, strides=1, padding='same'))
    model.add(Conv2D(filters=128, activation = 'relu', kernel_size=3, strides=1, padding='same'))
    model.add(GlobalAveragePooling2D())
    model.add(Dense(512, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(1))

    model.compile(
                loss='mean_squared_error',
                           optimizer='adam',
                          metrics=['mae', r2])
    return model


