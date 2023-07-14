'''
Linear regression using gradient descent to minimize squared error cost function.
'''
import numpy as np

def compute_gradient(X, y, w, b):
    m, n = X.shape
    dj_dw = np.zeros(n)
    dj_db = 0
    for i in range(m):
        try:
            y_hat = np.dot(X[i], w) + b
            dj_dw += (y_hat - y[i]) * X[i]
            dj_db += y_hat - y[i]
        except RuntimeWarning as w:
            print(f'X = {X}, y = {y}, w = {w}, b = {b}')

    dj_dw /= m
    dj_db /= m
    return dj_dw, dj_db

def gradient_descent(X, y, w_in, b_in, alpha, num_iters):
    w, b = w_in, b_in
    for i in range(num_iters):
        dj_dw, dj_db = compute_gradient(X, y, w, b)
        w -= alpha * dj_dw
        b -= alpha * dj_db
        if i % 100 == 0:
            print(f'Iteration {i}: w = {w}, b = {b}, cost={compute_cost(X, y, w, b)}')
    return w, b

def compute_cost(X, y, w, b):
    m = X.shape[0]
    cost = np.sum((np.matmul(X, w) + b - y) ** 2) / (2 * m)
    return cost

X = np.array([[20, 15], [10, 5], [5, 3], [6, 2], [8, 4]])
y = np.array([56, 23, 16, 15, 20.5])
initial_w = np.zeros(X.shape[1])
initial_b = 0
print(gradient_descent(X, y, initial_w, initial_b, 0.01, 1000))
print(gradient_descent(X, y, initial_w, initial_b, 0.01, 3000))
