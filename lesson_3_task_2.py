def a(n_1, n_2, n_3):
    s_n = n_1 + n_2 + n_3
    return s_n - min((n_1, n_2, n_3))
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = a(a, b, c)
print(d)
