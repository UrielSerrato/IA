import numpy as np
class Perpectron (object):
        #Parameters
        eta: float
        n_iter: int
        random_state: int       
        #Atributtes
        W_ : []
        errors_ : list

        #"""
        def __int__(self, eta=0.01, n_iter=50, random_state=1):
                 self.eta=eta
                 self.n_iter=n_iter
                 self.random_state=random_state

        def fit(self, X,y):
                  #"" Fit training data.
                  x: {array-like},shape = [n_samples, n_features]
                  y: array-like, shape = [n_samples]
                  self : object

        rgen = np.random.RandomState(self.random_state)
        self.w_=rgen.normal(loc=0.0, scale=0.01, size=1 + x.shape[1])

        self.errors_=[]

        for _ in range(self.n_iter):
                errors=0
                for xi, target in zip(x,y):
                        update = self.eta * (target - self.predict(xi))
                        self.w_[1:] += update * xi
                        self.w_[0] += update
                        errors +=int(update != 0.0)
                self.errors_.append(errors)
        return self

        def net_input(self, x):
                return np.dot(x, self.w_[1:]) + self.w_[0]

        def predict(self, x):
                return np.where(self.net_input(x) >= 0.0, 1, -1)

