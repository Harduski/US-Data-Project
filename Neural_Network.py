#Liberay
from keras.models import Sequential
from keras.layers import Dense
import numpy as np

#seed for reproducibility
np.random.seed(1000)
#load data
df = np.loadtxt(r'df_all.csv', delimiter=",")
#variables
size=df.shape
input= size[1]-1
#split input and output
X = df[:,0:input]
Y = df[:,input]

#creating model
model = Sequential()
model.add(Dense(60, input_dim=input, activation='sigmoid'))
model.add(Dense(30,  activation='sigmoid'))
model.add(Dense(1,  activation='sigmoid'))
#model compile
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
#fit the model
model.fit(X, Y, epochs=150, batch_size=100)
#evaluate Model
score=model.evaluate(X,Y)
print("\n %s: %.2f%%" % (model.metrics_names[1], score[1]*100))

#prediction
predictions = model.predict(X)
rounded = [round(x[0]) for x in predictions]
print(rounded)
