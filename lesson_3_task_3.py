print('Task#3')
def my_func(n_1, n_2, n_3):
    s_n = n_1 + n_2 + n_3
    return s_n - min(n_1, n_2, n_3)
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
print('Result: %s' % my_func(a, b, c))
