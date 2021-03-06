import numpy as np


class Perceptron:
    def __init__(self, N, alpha=0.01):
        # Divide W by the square-root of the number of inputs, a technique
        # used to scale the weight matrix leading to faster convergence
        self.W = np.random.randn(N + 1) / np.sqrt(N)
        self.alpha = alpha

    def step(self, x):
        return 1 if x > 0 else 0

    def fit(self, X, y, epochs=10):
        # Insert a column of 1s as bias
        X = np.c_[X, np.ones((X.shape[0]))]
        for _ in np.arange(0, epochs):
            for x, target in zip(X, y):
                # Pass the dot product of the feature vector with weight vector
                # to the step function
                pred = self.step(np.dot(x, self.W))
                if pred != target:
                    error = pred - target
                    self.W += -self.alpha * error * x

    def predict(self, X, add_bias=True):
        X = np.atleast_2d(X)
        if add_bias:
            X = np.c_[X, np.ones((X.shape[0]))]
        return self.step(np.dot(X, self.W))
