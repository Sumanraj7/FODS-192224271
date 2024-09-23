from sklearn.linear_model import LogisticRegression

X_train = [[200, 12], [300, 24], [150, 6]]
y_train = [0, 1, 0]

model = LogisticRegression()
model.fit(X_train, y_train)

new_customer = [[250, 18]]
print(model.predict(new_customer))
