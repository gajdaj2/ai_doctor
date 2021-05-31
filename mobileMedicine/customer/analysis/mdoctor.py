# Import required libraries
from functools import singledispatch

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn

# Import necessary modules
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from math import sqrt

# Keras specific
import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical


class MDoctor:

    def data_analysis(self, data_file, test):
        X_test, X_train, y_test, y_train, column_len = self.prepare_data(data_file)
        # create model
        model = self.create_model(column_len)
        # Compile the model
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        # build model
        self.build_model(X_test, X_train, model, y_test, y_train)
        out = model.predict([test])
        out1 = out.tolist()
        print("Wynik:"+str(out.tolist()))
        return out1[0][1], out1[0][0]

    def build_model(self, X_test, X_train, model, y_test, y_train):
        model.fit(X_train, y_train, epochs=20)
        pred_train = model.predict(X_train)
        scores = model.evaluate(X_train, y_train, verbose=0)
        print('Accuracy on training data: {}% \n Error on training data: {}'.format(scores[1], 1 - scores[1]))
        pred_test = model.predict(X_test)
        scores2 = model.evaluate(X_test, y_test, verbose=0)
        print('Accuracy on test data: {}% \n Error on test data: {}'.format(scores2[1], 1 - scores2[1]))

    def create_model(self, column_len):
        model = Sequential()
        model.add(Dense(500, activation='relu', input_dim=column_len - 1))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(50, activation='relu'))
        model.add(Dense(2, activation='softmax'))
        return model

    def prepare_data(self, data_file):
        df = pd.read_csv(data_file)
        columns_len = len(df.columns)
        df.describe()
        target_column = ['output']
        predictors = list(set(list(df.columns)) - set(target_column))
        df[predictors] = df[predictors] / df[predictors].max()
        df.describe()
        X = df[predictors].values
        y = df[target_column].values
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)

        # one hot encode outputs
        y_train = to_categorical(y_train)
        y_test = to_categorical(y_test)
        count_classes = y_test.shape[1]
        return X_test, X_train, y_test, y_train, columns_len
