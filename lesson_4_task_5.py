from functools import reduce
list = [i for i in range (100, 1001) if i % 2 == 0]
print('Even numbers: ', list)
print('Result: ', reduce(lambda a, b: a * b, list))

