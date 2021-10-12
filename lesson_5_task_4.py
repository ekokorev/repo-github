num = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('lesson_5_task_4_file.txt') as file, open('translate_lesson_5_task_4_file.txt', 'w') as new_file:
    file_text = file.readlines()
    for line in file_text:
        a = line.split()
        rus_num = num.get(a[0])
        new_file.write('%s' % line.replace(a[0], rus_num))
        



