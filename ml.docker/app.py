from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [20, 40, 60, 80, 100]

model = LinearRegression()
model.fit(X, y)

hours = 6
prediction = model.predict([[hours]])

print("Study Hours:", hours)
print("Predicted Score:", prediction[0])