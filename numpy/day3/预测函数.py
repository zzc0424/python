def predict(w, b, x):
    return w * x + b
xs = [1, 2, 3, 4, 5]
for x in xs:
    print(predict(2, 1, x))