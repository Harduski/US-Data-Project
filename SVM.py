from sklearn import svm
import numpy as np

#load data
df = np.loadtxt(r'df_all.csv', delimiter=",")

#variables
size = df.shape
input = size[1]-1

#split input and output
X = df[:,0:input]
Y = df[:,input]

#svm
model = svm.SVC(kernel='linear', decision_function_shape='ovr', C=0.01)
model.fit(X, Y)
predicted = model.predict(X)
score = model.score(X,Y)
print(predicted, score)




