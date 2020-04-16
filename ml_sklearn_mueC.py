from micromlgen import port
from sklearn.svm import SVC
from sklearn.datasets import load_iris
import numpy as np

iris = load_iris()
X = iris.data
y = iris.target
clf = SVC(kernel='linear').fit(X, y)
x=port(clf)
print(x)
text_file = open("sample.h", "w")
n = text_file.write(x)
text_file.close()

