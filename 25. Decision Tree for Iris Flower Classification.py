from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

iris = load_iris()
X_train, y_train = iris.data, iris.target

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

new_flower = [[5.1, 3.5, 1.4, 0.2]]
print(model.predict(new_flower))
