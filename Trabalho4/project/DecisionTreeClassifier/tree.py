from sklearn import tree, datasets, metrics
import numpy as np
import time

benning = time.time()

db = datasets.load_iris()

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

clf = tree.DecisionTreeClassifier(min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0,
                                  max_features=None, random_state=0, max_leaf_nodes=3, min_impurity_decrease=0.0, min_impurity_split=1e-7, class_weight=None, presort=False)

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
