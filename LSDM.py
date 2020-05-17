import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.layers import Flatten, LSTM, BatchNormalization
from tensorflow.keras.optimizers import SGD
from keras.callbacks import History 
import matplotlib.pyplot as plt

veri = pd.read_excel("merged_full.xlsx")

history = History()

label_encoder=LabelEncoder().fit(veri.Trafik_Indeks)
labels = label_encoder.transform(veri.Trafik_Indeks)
classes =list(label_encoder.classes_)

veri= veri.drop(["Tarih","Trafik_Indeks"],axis=1)
nb_features = 7
nb_classes=len(classes)

scaler = StandardScaler().fit(veri.values)
egitim_veri = scaler.transform(veri.values)


X_train, X_valid, y_train, y_valid = train_test_split(veri,labels,test_size=0.15)

y_train = to_categorical(y_train)
y_valid = to_categorical(y_valid)

X_train =np.array(X_train).reshape(340,7,1)
X_valid =np.array(X_valid).reshape(60,7,1)

model=Sequential()
model.add(LSTM(512,input_shape=(X_train.shape[1:])))
model.add(Activation("relu"))
model.add(BatchNormalization())
model.add(Flatten())
model.add(Dropout(0.25))
model.add(Dense(2048,activation="relu"))
model.add(Dense(1024,activation="relu"))
model.add(Dense(nb_classes,activation="softmax"))
model.summary()


model.compile(loss="categorical_crossentropy",optimizer="adam",metrics=["accuracy"])

model.fit(X_train, y_train, nb_epoch=100, batch_size=16, callbacks=[history])


plt.plot(model.history.history["accuracy"])
plt.title("Model Başarımları")
plt.ylabel("Başarım")
plt.xlabel("Epok")
plt.legend(["Egitim"],loc="upper left")
plt.show()

plt.plot(model.history.history["loss"],color = "red" )
plt.title("Model Kaybı")
plt.ylabel("Kayıp")
plt.xlabel("Epok")
plt.legend(["Kayıp"],loc="upper left")
plt.show()