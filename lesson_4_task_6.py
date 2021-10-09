from itertools import cycle, count
n = 50
list = [i for i in range(11)]
cou = count()
cyc = cycle(list)
print('Result: ', [next(cou) for i in range(n)])
print('Result', [next(cyc) for i in range(n)])




