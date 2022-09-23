word = input()
char = input()

for i in word:
    if i not in char.split(','):
        print(i, end='')
print('')