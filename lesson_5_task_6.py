total = {}
with open('lesson_5_task_6_file.txt') as file:
    file_text = file.readlines()
    for line in file_text:
        data = line.split()
        hours = 0
        for sign in data[1:]:
            if sign != '-':
                num = '0'
                for i in sign:
                    if i.isdigit():
                        num += i
                    else:
                        break
                hours += int(num)
        total.update({data[0].strip(':'): hours})

print(total)
