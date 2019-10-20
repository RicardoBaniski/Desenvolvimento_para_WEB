from sklearn import datasets, metrics, neural_network, svm
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt

db = datasets.load_boston()

X = db.data
Y = db.target

np.random.seed(0)

amostras = len(X)
divisao = 0.75

embaralhar = np.random.permutation(amostras)

X = X[embaralhar]
Y = Y[embaralhar]

X_treino = X[:int(amostras*divisao)]
Y_treino = Y[:int(amostras*divisao)]

X_teste = X[int(amostras*divisao):]
Y_teste = Y[int(amostras*divisao):]

parametros_svr = {'kernel': ('linear', 'poly', 'sigmoid', 'rbf'), 'C': [
    1, 2, 3, 4, 5]}

svr = svm.SVR()

clf = GridSearchCV(svr, parametros_svr, n_jobs=5, verbose=3)

clf.fit(X_treino, Y_treino)
print(clf.best_params_)

predicao = clf.predict(X_teste)

mse = metrics.mean_squared_error(Y_teste, predicao)
r2 = metrics.r2_score(Y_teste, predicao)

print('MSE:', mse)
print('R2:', r2)

clf1 = neural_network.MLPRegressor(hidden_layer_sizes=(23,))
clf1.fit(X_treino, Y_treino)
predicao_rede = clf.predict(X_teste)

mse_rede = metrics.mean_squared_error(Y_teste, predicao_rede)
r2_rede = metrics.r2_score(Y_teste, predicao_rede)

print('MLP')
print('MSE:', mse_rede)
print('R2:', r2_rede)

diagonal = list(range(int(min(Y_teste)), int(max(Y_teste))))

plt.title('Predicao: SVR')
plt.xlabel('Original')
plt.ylabel('Predicao')

plt.scatter(Y_teste, predicao)
plt.plot(diagonal, diagonal, 'r--')
plt.show()
