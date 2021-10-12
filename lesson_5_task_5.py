import random

with open('lesson_5_task_5_file.txt', 'w') as file:
    for i in range(20):
        file.write('%s' % random.randint(0, 10))


with open('lesson_5_task_5_file.txt') as file:
    num_str = file.read().split()
    s = 0
    for num in num_str:
        s += int(num)

print(s)
