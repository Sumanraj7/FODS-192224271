from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd

data = pd.read_csv('medical_data.csv')
X_train, y_train = data[['age', 'bp', 'cholesterol']], data['outcome']

model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)

X_test = [[45, 130, 200]]
y_pred = model.predict(X_test)
print(y_pred)
