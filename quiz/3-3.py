python = {'Alex': 83, 'Harry': 77, 'Davy': 93, 'Lisa': 65, 'Sunday': 89}
algorithm = {'Lisa': 91, 'Andrew': 88, 'Kevin': 76}
os = {'Harry': 60, 'Louis': 100, 'Mike': 90, 'Lisa': 58}

name = input()
flag = 0

if name in python:
    print(f'{name} gets {python[name]} on Python.')
    flag = 1
if name in algorithm:
    print(f'{name} gets {algorithm[name]} on Algorithm.')
    flag = 1
if name in os:
    print(f'{name} gets {os[name]} on OS.')
    flag = 1
if flag == 0:
    print(f'{name} is not taking any courses.')
