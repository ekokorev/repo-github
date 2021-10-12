with open('lesson_5_task_2_file.txt') as file:
    file_text = file.readlines()
    for numb, line in enumerate(file_text):
        w_count = len(line.split())
        print('Line № %s' % (numb + 1), 'Words: %s' % w_count)
        




