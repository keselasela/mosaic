import random
a = [1, 2, 3, 4, 5]
b = [3,4,5,6,7]
print(tuple(i/j for i, j in zip(a,b)))