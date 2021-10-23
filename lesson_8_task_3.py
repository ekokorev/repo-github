class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):


        while True:
            try:
                val = int(input('Input any number and enter - '))
                self.my_list.append(val)
                print(f'Current list - {self.my_list} \n ')
            except:
                print(f"Impossible!")
                y_or_n = input(f'try again? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Exit'
                else:
                    return f'Exit'


try_except = Error(1)
print(try_except.my_input())


