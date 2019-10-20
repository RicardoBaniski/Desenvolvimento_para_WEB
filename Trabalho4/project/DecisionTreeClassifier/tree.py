from sklearn import tree, datasets, metrics
import numpy as np
import time

benning = time.time()

db = datasets.load_digits()

X = db.data  # atributos
Y = db.target  # classe

np.random.seed(10)

n_samples = len(X)
particao = 0.75

order = np.random.permutation(n_samples)

X = X[order]
Y = Y[order]

X_treino = X[:int(n_samples*particao)]
Y_treino = Y[:int(n_samples*particao)]

X_teste = X[int(n_samples*particao):]
Y_teste = Y[int(n_samples*particao):]

clf = tree.DecisionTreeClassifier(
    criterion='entropy', random_state=1000, min_impurity_split=1e-1)

tree.plot_tree(clf.fit(X_treino, Y_treino))
predict_ = clf.predict(X_teste)

print('\nBase:\n', predict_)

print('\nAccuracy:', (clf.score(X_teste, Y_teste))*100, '%')

matriz = metrics.confusion_matrix(Y_teste, predict_)

print('\nArray:')
for linha in matriz:
    print(linha)

end = time.time()
print('\nRun time: ', end-benning, 'ms\n')
