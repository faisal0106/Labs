from sklearn.linear_model import LinearRegression
import numpy as np
x = np.array([1,2,3,4,5]).reshape(-1,1)
y = np.array([2,4,6,8,10])
model = LinearRegression()
model.fit(x,y)
print(model.predict([[6]]))
