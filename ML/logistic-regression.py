from sklearn.linear_model import LogisticRegression
x = [[1],[2],[3],[4]]
y = [0,1,0,1]
model = LogisticRegression()
model.fit(x,y)
print(model.predict([[5]]))
