##############################################
#--- Day 1: Not Quite Lisp ---
#--- part one ---
#For example:
#
#    (()) and ()() both result in floor 0.
#    ((( and (()(()( both result in floor 3.
#    ))((((( also results in floor 3.
#    ()) and ))( both result in floor -1 (the first basement level).
#    ))) and )())()) both result in floor -3.
#
#Question - To what floor do the instructions take Santa?
##############################################

#floor = 0
#with open("test_case_day_1.1.txt", 'r') as file:
#    for data in file:
#        for move in data:
#            if move == '(':
#                floor += 1
#            elif move == ')':
#                floor -= 1
#
#    print(floor)

#############################################
#--- Part Two ---

#Now, given the same instructions, find the position of the first character that causes him to enter the basement (floor -1). The first character in the instructions has position 1, the second character has position 2, and so on.
#
#For example:
#
#    ) causes him to enter the basement at character position 1.
#    ()()) causes him to enter the basement at character position 5.
#
#Question - What is the position of the character that causes Santa to first enter the basement?
############################################

floor = 0
count = 0
with open("test_case_day_1.1.txt", 'r') as file:
    for data in file:
        for move in data:
            count += 1
            if move == '(':
                floor += 1
            elif move == ')':
                floor -= 1
            if floor == -1:
                break
    print(count)

