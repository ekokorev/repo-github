print('Task#5')
def sum(n_st, stop):
    n_list = n_st.split(' ')
    sum = 0
    for i in n_list:
        if i == stop:
            break
        sum  += int(i)
    return sum
stop_symb = '%'
fin = False
s = 0
while not fin:
    n_st_user = input('Enter any numbers separated by " ": ')
    s += sum(n_st_user, stop_symb)
    fin = stop_symb in n_st_user
    print('%s' % s)