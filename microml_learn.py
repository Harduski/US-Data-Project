from micromlgen import port
import sklearn.svm as svm

from sklearn.datasets import load_iris


if __name__ == '__main__':
    iris = load_iris()
    X1, X_test = iris.data[:-10, :], iris.data[-10:, :]
    Y1, y_test = iris.target[:-10], iris.target[-10:]
    clf = svm.SVC(kernel='linear', decision_function_shape='ovr', C=0.01, gamma=0.001)
    clf.fit(X1, Y1)



    print(port(clf))