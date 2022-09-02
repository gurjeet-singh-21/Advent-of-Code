#--- Day 10: Elves Look, Elves Say ---

from itertools import groupby

#input = '1'  #  test case
input = '1113122113'

#for i in range(40): # part one
for i in range(50): # part two
    output = ''
    
    new = groupby(input)

    for j,k in new:
        output += str(len(list(k))) + j

    #print(f'{input} becomes {output}')
    input = output
print(len(output))



#1 becomes 11 (1 copy of digit 1).
#11 becomes 21 (2 copies of digit 1).
#21 becomes 1211 (one 2 followed by one 1).
#1211 becomes 111221 (one 1, one 2, and two 1s).
#111221 becomes 312211 (three 1s, two 2s, and one 1)
