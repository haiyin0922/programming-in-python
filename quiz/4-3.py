def final_grade(quiz1=0, quiz2=0, quiz3=0, quiz4=0, quiz5=0, exam=0): # Replace XXXXX with your parameter definition
    # YOUR CODE
    result = quiz1 * 0.1 + quiz2 * 0.1 + quiz3 * 0.1 + quiz4 * 0.1 + quiz5 * 0.1 + exam * 0.5
    print(f'{result:.1f}')

exec(input()) # MUST ADD THIS LINE!!