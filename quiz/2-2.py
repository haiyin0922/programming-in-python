name = input()
sport = input()

print(f'My nickname is "{name}".')
print('I\'m good at ', end='')
for i in sport.split():
    print(f'{i}, ', end='')
print('etc.')