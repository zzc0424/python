data = list(range(100))
n = len(data)
train = data[:int(n * 0.8)]
val = data[int(n * 0.8) : int(n * 0.9)]
test = data[int(n * 0.9) :]
print(len(train))
print(len(val))
print(len(test))