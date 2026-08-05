import numpy as np
A = np.array([[1, 2],[3, 4],[5, 6]])
B = np.array([[1, 2, 3],[4, 5, 6]])
c = A @ B
print(c.shape)
print(c[0, 0])