def mse(w, b, xs, ys):
    total = 0
    for x, y in zip(xs,ys):
        pred = w * x + b
        total += (pred - y) ** 2
    return total / len(xs)
def step(w, b, xs, ys, lr = 0.01):
    n = len(xs)
    dw = 0
    db = 0
    for x, y in zip(xs, ys):
        pred = w * x + b
        err = pred - y
        dw += 2 * err * x
        db += 2 * err
    w = w - lr * dw / n
    b = b - lr * db / n
    return w, b
xs = [1, 2, 3, 4, 5]
ys = [3, 5, 7, 9, 11]
w = 0
b = 0
lr = 0.01
for i in range(1000):
    w, b = step(w, b, xs, ys, lr)
    print(f"第{i+1}步: w = {w}, b = {b}, 损失 = {mse(w, b, xs, ys)}")