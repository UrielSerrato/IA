import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from numpy.random import seed

class AdalineSGD(object):

    data = pd.DataFrame({
        'X1': np.random.randn(100),
        'X2': np.random.randn(100),
        'y': np.where(np.random.randn(100) > 0, 1, -1)
    })

    X = data[['X1', 'X2']].values
    y = data['y'].values

    adaline = AdalineSGD(eta=0.01, n_iter=50, random_state=1)

    adaline.fit(X, y)

    plt.plot(range(1, len(adaline.cost_) + 1), adaline.cost_, marker='o')
    plt.xlabel('Iteraciones')
    plt.ylabel('Costo')
    plt.title('Entrenamiento de AdalineSGD')
    plt.show()

    from matplotlib.colors import ListedColormap

    def plot_decision_regions(X, y, classifier, resolution=0.02):
        markers = ('s', 'x', 'o', '^', 'v')
        colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
        cmap = ListedColormap(colors[:len(np.unique(y))])

        x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1

        xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                            np.arange(x2_min, x2_max, resolution))

        Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
        Z = Z.reshape(xx1.shape)

        plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
        plt.xlim(xx1.min(), xx1.max())
        plt.ylim(xx2.min(), xx2.max)

        for idx, cl in enumerate(np.unique(y)):
            plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                        alpha=0.8, c=colors[idx],
                        marker=markers[idx], label=cl, edgecolor='black')

    plot_decision_regions(X, y, classifier=adaline)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.legend(loc='upper left')
    plt.title('Línea de decisión de AdalineSGD')
    plt.show()
