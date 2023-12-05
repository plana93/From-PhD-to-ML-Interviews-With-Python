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
        self.B = None

    def fit(self,
            X,
            y,
            lr=0.01,
            num_iter = 1000
            ):
        self.W = np.zeros((X.shape[1], 1))
        self.B = 0

        for iter_ in range(num_iter):
            y_pred = np.dot(X, self.W) + self.B
            y_pred = y_pred.reshape(-1)
            cost_function = np.sum((y_pred - y)**2)  +  self.regul * np.sum(self.W ** 2)
            gradient_w  = (1 / len(X)) * 2 *  np.sum(np.dot(X.T, (y_pred - y))) + 2*self.regul*np.sum(self.W)
            gradient_b  = (1 / len(X)) * 2 *  np.sum(y_pred - y)
            self.W = self.W - lr*gradient_w
            self.B = self.B - lr*gradient_b

    def predict(self, X):
        y_pred = np.dot(X, self.W) + self.B
        return y_pred

X = np.array([[1, 2, 3, 4, 5]]).T
Y = np.array(y)
lin_reg = LinReg(0.1)
lin_reg.fit(X, y, lr=0.01, num_iter=10000)
y_pred = lin_reg.predict(X)

print("Bias and Weight with GD", [lin_reg.B, lin_reg.W[0][0]] )