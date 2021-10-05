print('Task#1')
def num(a, b):
    if b == 0:
        return 'Divide to "0" is not possible!'
    else:
        return a / b

a = int(input('Any integer a: '))
b = int(input('Any integer b: '))
print('Result %s' % num(a, b))



