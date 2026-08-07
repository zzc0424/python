import os

import numpy as np
import matplotlib.pyplot as plt


def make_data(n=100, seed=42):
    np.random.seed(seed)
    xs = np.random.rand(n) * 10
    ys = 2 * xs + 3 + np.random.randn(n)
    return xs, ys


def train(xs, ys, lr=0.01, steps=1000):
    w = 0
    b = 0
    history = []
    for i in range(steps):
        pred = w * xs + b
        err = pred - ys
        loss = np.mean(err ** 2)
        history.append(loss)
        w = w - lr * np.mean(2 * err * xs)
        b = b - lr * np.mean(2 * err)
    return w, b, history


def plot_results(xs, ys, w, b, history):
    os.makedirs("images", exist_ok=True)

    plt.scatter(xs, ys, alpha=0.5, label="data")
    line_x = np.linspace(0, 10, 100)
    plt.plot(line_x, w * line_x + b, color="red", label="fit")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.savefig("images/figure_1.png")
    plt.show()

    plt.plot(history)
    plt.xlabel("step")
    plt.ylabel("loss")
    plt.title("Loss Curve")
    plt.savefig("images/figure_2.png")
    plt.show()


def main():
    xs, ys = make_data()
    w, b, history = train(xs, ys)
    print(f"w = {w:.4f}")
    print(f"b = {b:.4f}")
    print(f"最终损失 = {history[-1]:.6f}")
    plot_results(xs, ys, w, b, history)


if __name__ == "__main__":
    main()