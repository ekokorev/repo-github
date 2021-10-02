print('Task#1')

data = [4, 7, 'abcdefghijk', [9, 8, 7, 6, 5, 4], (3, 2), {'f': 5}]
for a in data:
    print(type(a))



print('Task#2')

user_data = input('Enter any data: ')
input_data = user_data.split()
len_data = len(input_data)
b = 0
while b <len_data - 1:
        c = input_data[b]
        input_data[b] = input_data[b+1]
        input_data[b+1] = c
        b += 2
print(input_data)


print('Task#3')

month = input('Enter month number - ')
d, e, f, g = 'winter', 'spring', 'summer', 'autumn'
m_dict = {'1': d, '2': d, '12': d, '3': e, '4': e, '5': e, '6': f, '7': f, '8': f, '9': g, '10': g, "11": g}
print(m_dict[month].upper())


print('Task#4')

w_input = input('Enter some words: ')
words = w_input.split()
for n, w in enumerate(words):
    print(('#%s' % n), ('- %s' % w[:10]))


print('Task#5')

my_list = [7, 5, 3, 3, 2]
rating = int(input('Enter Rating - '))
ins = False
for ind, elem in enumerate(my_list):
    if rating > elem:
        my_list.insert(ind, rating)
        ins = True
        break
if not ins:
    my_list.append(rating)
print(my_list)



print('Task#6')

prod = []
count = 1
command = ''
while command != 'stop':
    item_name = input('Item name - ')
    item_price = input('Item price - ')
    item_amount = input('Item amount - ')
    item_unit = input('Item units - ')
    prod.append((count, {'Item name': item_name, 'Item price': item_price, 'Item amount': item_amount, 'Item units': item_unit}))
    count += 1
    command = input('Write "stop" for interrupting - ')
total_list = {}
for numb, item_dict in prod:
    for key, value in item_dict.items():
        if not total_list.get(key):
            total_list[key] = [value]
        else:
            total_list[key].append(value)
for key, value in total_list.items():
    total_list[key] = list(set(value))
print(total_list)











