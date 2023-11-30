import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]
f_x = []

n = len(x)
assert n == len(y)

sumX = 0
sumX2 = 0
sumY = 0
sumXY = 0

# one shot
for i in range(n):
    sumX += x[i]
    sumX2 += x[i]**2
    sumY += y[i]
    sumXY += x[i] * y[i]

m = (n * sumXY - sumX * sumY)/(n*sumX2 - sumX * sumX)
bias = (sumY - m * sumX)/n

for i in range(max(x)):
    f_x.append(m*i + bias)

print("Bias and Weight with one shot : ", [bias, m])

plt.scatter(x, y, color='blue', label='input')
plt.scatter(x, y, color='red', label='output')
plt.plot([i for i in range(max(x))], f_x, color='green', label='regression line')

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Linear Regression')
plt.legend()
#plt.show()


# gradient descent

class LinReg:
    def __init__(self, regul = 0 ):
        self.regul = regul
        self.W = None

    def fit(self,
            X,
            y,
            lr=0.01,
            num_iter = 1000
            ):
        X = np.hstack([np.ones((len(X), 1)), X])
        self.W = np.zeros(X.shape[1])

        for iter_ in range(num_iter):
            y_pred = np.dot(X, self.W)
            cost_function = np.sum((y_pred - y)**2)  +  self.regul * np.sum(self.W ** 2)
            gradient  = 2 * np.dot(X.T, (y_pred - y)) + 2*self.regul*self.W
            self.W = self.W - lr*gradient

    def predict(self, X):
        X = np.hstack([np.ones((len(X), 1)), X])
        y_pred = np.dot(X, self.W)
        return y_pred

X = np.array([[1, 2, 3, 4, 5]]).T
Y = np.array(y)
lin_reg = LinReg(0.1)
lin_reg.fit(X, y, lr=0.001, num_iter=10000)
y_pred = lin_reg.predict(X)

print("Bias and Weight with GD", lin_reg.W)