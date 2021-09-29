print('Task#2')

a = int(input('Enter time in seconds: '))
if a < 60:
    print(f'00:00:{a:02}')
elif a < 3600:
    print(f'00:{a // 60:02}:{a % 60:02}')
else:
    print(f'{a // 3600:02}:{(a % 3600) // 60:02}:{a % 60:02}')


print('Task#3')

b = input('Enter any integer number: ')
c = int(b) + int(b*2) + int(b*3)
print('Sum: %s' % c)

print('Task#4')

num = int(input('Enter any positive integer number: '))
max_num = 0
while num > 0:
    if num % 10 > max_num:
        max_num = num % 10
        if max_num == 9:
            break
    num = num // 10
print('Max number: %s' % max_num)


print('Task#5')

earn = int(input('Earning: '))
cost = int(input('Costs: '))
if cost > earn:
    print('Loss')
elif earn > cost:
    print('Profit')
    efficiency = (earn - cost) / earn
    print('Efiiciency: %s' % efficiency)
    emp_num = int(input('Employees number: '))
    prof_per_emp = (earn - cost) / emp_num
    print('Profit per employee: %s' % prof_per_emp)
elif earn == cost:
    print('Financial result = 0')



print('Task#6')

dist = float(input('First day distance: '))
goal = float(input('Goal: '))
day = 1
while dist < goal:
    dist *= 1.1
    day += 1
print('Days required: %s' % day)







