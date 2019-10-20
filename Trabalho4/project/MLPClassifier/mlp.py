from sklearn import neural_network, datasets, metrics
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

clf = neural_network.MLPClassifier(
    hidden_layer_sizes=(150,), alpha=0.001, n_iter_no_change=3)

clf.fit(X_treino, Y_treino)
predicao = clf.predict(X_teste)

print('\nAccuracy:', (clf.score(X_teste, Y_teste))*100, '%')

print('\nBase:', predicao)

matriz = metrics.confusion_matrix(Y_teste, predicao)

print('\nArray:')
for linha in matriz:
    print(linha)

# pesos
#print('\nPesos: ')
# print(clf.coefs_)
# perda de informação
print('\nPerda de Informação:')
print(clf.loss_)
# print(clf.intercepts_)

end = time.time()
print('\nRun time: ', end-benning, 'ms\n')
