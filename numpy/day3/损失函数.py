def mse(w, b, xs, ys):
    total = 0
    for x, y in zip(xs,ys):
        pred = w * x + b
        total += (pred - y) ** 2
    return total / len(xs)
xs = [1, 2, 3, 4, 5]
ys = [3, 5, 7, 9, 11]
print(mse(2, 1, xs, ys))
print(mse(0, 0, xs, ys))