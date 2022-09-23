reversed_L = []

def reverse_list(L):
    # YOUR CODE
    for i in L:
        if type(i) == list:
            reverse_list(i)
        else:
            reversed_L.insert(0, i)
    return reversed_L

print(eval(input())) # MUST add this line
