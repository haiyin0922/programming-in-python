a = input()
b = input()

try:
    quotient = int(a)/int(b)
except ValueError:
    print('Integer inputs only')
except ZeroDivisionError:
    print('Cannot divide by 0')
else:
    print(f'{quotient:.2f}')