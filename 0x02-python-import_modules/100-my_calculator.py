#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as cal
    count = len(sys.argv)
    if count == 4:
        a = sys.argv[1]
        b = sys.argv[3]
        c = sys.argv[2]
        if c == '+':
            print('{} + {} = {}'.format(a, b, cal.add(int(a), int(b))))
        elif c == '-':
            print('{} - {} = {}'.format(a, b, cal.sub(int(a), int(b))))
        elif c == '*':
            print('{} * {} = {}'.format(a, b, cal.mul(int(a), int(b))))
        elif c == '/':
            print('{} / {} = {}'.format(a, b, cal.div(int(a), int(b))))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
