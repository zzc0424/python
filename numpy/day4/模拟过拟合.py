xs = [1, 2, 3, 4, 5]
ys = [3, 5, 7, 9, 11]
train_x = xs[:4]   
train_y = ys[:4]   
test_x = xs[4:]    
test_y = ys[4:]    
memory = {}
for x, y in zip(train_x, train_y):
    memory[x] = y

def lookup_model(x):
    if x in memory:
        return memory[x]   
    else:
        return None  
for x in xs:
    print(lookup_model(x) )   
print(lookup_model(5))  