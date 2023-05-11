import dataset
X, Y = dataset.load_linear_example1()

print(f'{X=}')
print(f'{Y=}')

#ver1のtest
import regression
model = regression.LinearRegression()
print(model.x)

#ver2のtest
import importlib
importlib.reload(regression)
model = regression.LinearRegression()
model.fit(X, Y)
print(model.theta)

#ver3のtest
model = regression.LinearRegression()
model.fit(X, Y)
print(model.predict(X))

#ver4のtest
model = regression.LinearRegression()
model.fit(X, Y)
print(model.score(X, Y))