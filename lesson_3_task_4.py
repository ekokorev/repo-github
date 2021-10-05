print('Task#4')


def a(x, y):
    if x < 0:
        return '"x" must be grater than 0!'
    if y > 0:
        return '"y" must be less than 0!'
    z = 1
    for i in range(y * -1):
        z *= x
    return 1 / z


x = float(input('Enter any positive number - x: '))
y = int(input('Enter any negative integer - y: '))
print('Result: %s' % a(x, y))
