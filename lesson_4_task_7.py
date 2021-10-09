def gen_fact(num):
    a = 1
    for i in range(1, num + 1):
        a *= i
        yield a

n = 12
for b, c in enumerate(gen_fact(n)):
    print('n! %s' % (b + 1), '= %s' % c)
