def pascal(row, col):
    # YOUR CODE
    if col == 0 or col == row:
        return 1
    else:
        num = pascal(row-1, col-1) + pascal(row-1, col)
        return num

def print_pascal(n):
    # YOUR CODE
    for i in range(n):
        for j in range(i+1):
            num = pascal(i, j)
            print(f'{num:3d}', end='')
        print('')

exec(input()) # MUST add this line