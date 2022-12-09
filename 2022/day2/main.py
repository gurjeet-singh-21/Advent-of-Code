# --- Day 2: Rock Paper Scissors ---

# 'A','B','C' = 'rock','paper','scissors'
# 'X','Y','Z' = 'rock','paper','scissors'
# rock, paper, scissors = 1,2,3
 
info = {'A':['rock', 1], 'B':['paper', 2], 'C':['scissors',3], 
        'X':['rock', 1], 'Y':['paper', 2], 'Z':['scissors',3]}



loss, draw, win = 0,3,6

total = 0

#with open('ex2.txt', 'r') as file:
with open('input2.txt', 'r') as file:
    data = [i.strip().split() for i in file]

#for i in data:
#    if i[0] == 'A' and i[1] == 'Y':
#        total += win + info[i[1]][1]
#
#    elif i[0] == 'A' and i[1] == 'Z':
#        total += loss + info[i[1]][1]
#
#    elif i[0] == 'A' and i[1] == 'X':
#        total += draw + info[i[1]][1]
## -------
#    if i[0] == 'B' and i[1] == 'Y':
#        total += draw + info[i[1]][1]
#
#    elif i[0] == 'B' and i[1] == 'Z':
#        total += win + info[i[1]][1]
#
#    elif i[0] == 'B' and i[1] == 'X':
#        total += loss + info[i[1]][1]
## -------
#    if i[0] == 'C' and i[1] == 'Y':
#        total += loss + info[i[1]][1]
#
#    elif i[0] == 'C' and i[1] == 'Z':
#        total += draw + info[i[1]][1]
#
#    elif i[0] == 'C' and i[1] == 'X':
#        total += win + info[i[1]][1]
# -------
#print(total)

# --- Part Two ---

info2 = {'A':['rock', 1], 'B':['paper', 2], 'C':['scissors',3]}

for i in data:
    if i[0] == 'A' and i[1] == 'Y':
        total += draw + info2['A'][1]

    elif i[0] == 'A' and i[1] == 'Z':
        total += win + info2['B'][1]

    elif i[0] == 'A' and i[1] == 'X':
        total += loss + info2['C'][1]
# -------
    if i[0] == 'B' and i[1] == 'Y':
        total += draw + info2['B'][1]

    elif i[0] == 'B' and i[1] == 'Z':
        total += win + info2['C'][1]

    elif i[0] == 'B' and i[1] == 'X':
        total += loss + info2['A'][1]
# -------
    if i[0] == 'C' and i[1] == 'Y':
        total += draw + info2['C'][1]

    elif i[0] == 'C' and i[1] == 'Z':
        total += win + info2['A'][1]

    elif i[0] == 'C' and i[1] == 'X':
        total += loss + info2['B'][1]
#---------
print(total)
