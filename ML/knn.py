from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
X,y = load_iris(return_X_y = True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
print("Model Accuracy: ", model.score(X_test,y_test))
