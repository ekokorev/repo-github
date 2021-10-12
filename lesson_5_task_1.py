with open('task_1_lesson_5.txt', 'w') as file:
    input_text = input('Text:\n')
    while input_text:
        file.write(f'{input_text}\n')
        input_text = input('Text:\n')

