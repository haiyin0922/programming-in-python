def CharRange(start, end):
    # Your code here to yield one character at a time
    for i in range(abs(ord(end) - ord(start)) + 1):
        if ord(end)-ord(start) > 0: 
            yield chr(ord(start) + i)
        else:
            yield chr(ord(start) - i)

# For judging purpose
instantiate_generator1 = input()
exec(instantiate_generator1)
instantiate_generator2 = input()
exec(instantiate_generator2)
for i in range(4):
    test_code = input()
    exec(test_code)