from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from joblib import dump, load

#load data
df = np.loadtxt(r'df_all.csv', delimiter=",")

#variables
size = df.shape
input = size[1]-1

#split input and output
X = df[:,0:input]
Y = df[:,input]

# NearestNeighbors
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X, Y)
string_bayes = model.get_params(deep='true')


dump(model, 'filename.joblib')
clf = load('filename.joblib')
# file creation
#  new_file = open(r'svm_classi.txt', 'w+')
# new_file.write(string_bayes)
# new_file.close()

predicted = model.predict(X)



print(predicted)



