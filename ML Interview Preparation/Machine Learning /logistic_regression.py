import numpy as np
import matplotlib.pyplot as plt


class Logistic_Regression:
    def __init__(self, regularizer=0):
        self.regularizer = regularizer
        self.weights = None
        self.bias = None

    def fit(self,
            X_input,
            y_output,
            lr=0.01,
            num_iter=1000
            ):

        self.weights = np.zeros((X_input.shape[1], 1))  # shape (2,1)
        self.bias = 0
        #import pdb
        #pdb.set_trace()
        for iter_ in range(num_iter):
            y_pred_pre_activation = np.dot(X_input, self.weights) + self.bias  # size 5.1
            y_output = y_output.reshape(-1,1) # size (5,)
            y_pred = (1 / (1 + np.exp(-y_pred_pre_activation)))

            cost_function = - (1 / len(X_input)) * \
                            np.sum(
                                y_output * np.log(y_pred)  + \
                                (1-y_output) * np.log( 1 - y_pred)) + \
                            self.regularizer * np.sum(self.weights ** 2)


            gradient_w = (1 / len(X_input)) * \
                         np.sum(
                             ((1 / (1 + np.exp(-y_pred_pre_activation))) -
                             y_output) * X_input
                          ) + 2 * self.regularizer * np.sum(self.weights)


            gradient_b = (1 / len(X_input)) * np.sum(
                             ((1 / (1 + np.exp(-y_pred_pre_activation))) -
                             y_output))
            self.weights = self.weights - lr * gradient_w
            self.bias = self.bias - lr * gradient_b

            if iter_ % 10 == 0: print(cost_function)

    def predict(self, X):
        y_pred = np.dot(X, self.weights) + self.bias
        y_pred = (1 / (1 + np.exp(-y_pred)))
        return np.round(y_pred).astype(int)


# create sample dataset
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 0, 1, 1, 1])

# initialize logistic regression model
lr = Logistic_Regression(regularizer=0.1)

# train model on sample dataset
lr.fit(
    X_input=X,
    y_output=y,
    lr=0.01,
    num_iter=1000
)

# make predictions on new data
X_new = np.array([[6, 7], [7, 8]])
y_pred = lr.predict(X_new)

# create 2D dataset
X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y = np.array([0, 0, 1, 1, 1])
# initialize logistic regression model
lr = Logistic_Regression(regularizer=0.1)

# train model on sample dataset
lr.fit(
    X_input=X,
    y_output=y,
    lr=0.01,
    num_iter=1000
)

print(y_pred)  # [1, 1]

# plot decision boundary
x1 = np.linspace(0, 6, 100)
x2 = np.linspace(0, 8, 100)
xx, yy = np.meshgrid(x1, x2)
Z = lr.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Spectral, alpha=0.8)

# plot data points
plt.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.Spectral)

plt.show()