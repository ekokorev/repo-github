import sys
if len(sys.argv) < 4:
    print('Enter all the data (output, wage-rate, bonus):')
else:
    out = float(sys.argv[1])
    w_r = float(sys.argv[2])
    bon = float(sys.argv[3])
    salary = out * w_r + bon
    print(salary)