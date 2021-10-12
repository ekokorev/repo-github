import json

firms = {}
pos_count, pos_sum = 0, 0
with open('lesson_5_task_7.txt') as file:
    file_text = file.readlines()
    for line in file_text:
        data = line.split()
        profit = float(data[2]) - float(data[3])
        firms.update({data[0]: profit})
        if profit > 0:
            pos_count += 1
            pos_sum += profit

aver_profit = pos_sum / pos_count
result = [firms, {'aver_profit': aver_profit}]

with open('lesson_5_task_7_json.txt', 'w') as file:
    json.dump(result, file)