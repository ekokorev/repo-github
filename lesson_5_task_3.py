with open('employees_salary.txt') as file:
    file_text = file.readlines()
    emp = {}
    sum_salary = 0
    for line in file_text:
        emp_info = line.split()
        emp.update({emp_info[0]: float(emp_info[1])})
        sum_salary += float(emp_info[1])
average_sal = sum_salary / len(emp)
print('Average salary: %s' % average_sal)

for a, b in emp.items():
    if b < 20000:
        print('%s' % a, '%s' % b)
        

