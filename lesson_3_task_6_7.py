print('Task#6_7')
def int_func(txt):
    a = txt[0].upper() + txt[1:].lower()
    return a
str = input('Enter words separate by " ": ')
for a in str.split(' '):
    print('%s' % int_func(a), end=' ')