from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array([[1,2],[2,3],[3,4],[4,5]])
y = np.array([1,2,3,4])
model = LinearRegression()
model.fit(x,y)
print(model.predict([[5,6]]))
