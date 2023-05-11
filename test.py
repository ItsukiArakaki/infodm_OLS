import dataset
X, Y = dataset.load_linear_example1()

print(f'{X=}')
print(f'{Y=}')

import regression
model = regression.LinearRegression()
print(model.x)

import importlib
importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X, Y)
print(model.theta)