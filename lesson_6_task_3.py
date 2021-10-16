class Worker:
    def __init__(self, name, surname, position, salary, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'salary': salary, 'bonus': bonus}

class Position(Worker):

    def get_full_name(self):
        return '%s' % self.name, '%s' % self.surname

    def get_total_income(self):
        return print('Total salary - ', self._income['salary'] + self._income['bonus'])

employee = Position('John', 'Smith', 'Physician', 70000, 10000)
print(employee.name, employee.surname, '-', employee.position)
print(employee._income)
print(employee.get_total_income())
