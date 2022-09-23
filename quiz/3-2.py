lines = []

for i in range(4):
    line = input()
    year = int(line) # Convert to integer
    lines.append(year) # Add to list

for year in lines:
    # YOUR CODE HERE
    if year % 4 == 0:
        if year % 400 == 0:
            print(f'{year} is a leap year.')
        elif year % 100 == 0:
            print(f'{year} is a common year.')
        else:
            print(f'{year} is a leap year.')
    else:
        print(f'{year} is a common year.')
    