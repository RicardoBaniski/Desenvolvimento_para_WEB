from sklearn import datasets, metrics
from sklearn.linear_model import Perceptron
import numpy as np
import time

benning = time.time()

digits_ = datasets.load_digits()

X = digits_.data
Y = digits_.target

np.random.seed(0)

n_samples = len(X)
percentage = 0.75

order = np.random.permutation(n_samples)
X = X[order]
Y = Y[order]

Y_test = Y[int(percentage*n_samples):]
X_test = X[int(percentage*n_samples):]

Y_training = Y[:int(percentage*n_samples)]
X_training = X[:int(percentage*n_samples)]

print('\n*** MÉTODO PERCEPTRON ***')

clf = Perceptron(penalty=None, alpha=0.0001, max_iter=1000)
clf.fit(X_training, Y_training)
predict_ = clf.predict(X_test)
print('\nBase:')
print(predict_)

accuracy = clf.score(X_test, Y_test)
print('\nAccuracy: ', accuracy*100, '%')

array = metrics.confusion_matrix(Y_test, predict_)
print('\nArray:')
for item in array:
    print(item)

end = time.time()
print('\nRun time: ', end-benning, 'ms\n')
