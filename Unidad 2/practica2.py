import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lee el conjunto de datos desde un archivo CSV
df = pd.read_csv('C:\Users\hp\Desktop\Modificado\serrato_archivo.csv')

# Codifica las etiquetas de clase 'Masculino', 'Femenino' a valores numéricos
df['Genero'] = df['Genero'].map({'Masculino': 0, 'Femenino': 1})

# Dividir el conjunto de datos en características (X) y etiquetas (y)
X = df[['Masa Muscular', 'Grasa Corporal']].values  # Usamos Masa Muscular y Grasa Corporal como características
y = df['Genero'].values     # La etiqueta de clase es 'Genero'

class Perceptron(object):
    def __init__(self, eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter

    def fit(self, X, y):
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def predict(self, X):
        """Return class label after unit step"""
        return np.where(self.net_input(X) >= 0.0, 0, 1)  # Usamos 0 para Masculino y 1 para Femenino

# Crear una instancia del perceptrón y entrenarlo
perceptron = Perceptron(eta=0.1, n_iter=100)
perceptron.fit(X, y)

# Crear un gráfico de dispersión para mostrar la clasificación
colors = ['red', 'green', 'blue']
markers = ['o', 's', 'x']
for tipo in np.unique(y):
    plt.scatter(X[y == tipo][:, 0], X[y == tipo][:, 1], color=colors[tipo], marker=markers[tipo], label=tipo)

# Realizar predicciones
nuevo_dato = np.array([32, 16.2])  # Ejemplo de un nuevo dato de MM y GP de una persona
prediccion = perceptron.predict(nuevo_dato)

# Convertir la predicción a tipo de genero
tipo_de_genero = ['Masculino', 'Femenino']
tipo_predicho = tipo_de_genero[prediccion]

plt.scatter(nuevo_dato[0], nuevo_dato[1], color='blue', marker='*', s=200, label=f'Predicción: {tipo_predicho}')
plt.xlabel('Masa Muscular')
plt.ylabel('Grasa Corporal')
plt.legend()
plt.show()