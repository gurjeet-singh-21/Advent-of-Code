# --- Day 5: Supply Stacks ---

#with open('ex5.txt', 'r') as file:
with open('input5.txt', 'r') as file:

    stacking, movement = (i.splitlines() for i in file.read().split('\n\n'))

#print(stacking)
#print(movement)

index = [i for i, char in enumerate(stacking[-1]) if char != ' ']
stacks = {int(i):[] for i in stacking[-1].replace(' ', "")}

#print(stacks)
#print(index)

for i in stacking[:-1]:
    count = 1
    for j, c in enumerate(i):
#        if c != ' ' and j in index:
#            print(c, j)
        if j in index:
            stacks[count] += c
            count += 1

for values in stacks.values():
    while True:
        if ' ' in values:
            values.remove(' ')
        elif ' ' not in values:
            break
#print(stacks) 

movement = [i.replace('move','').replace('from','').replace('to','').split() for i in movement]

#print(movement)

#for i in movement:
#    count, from_, to_ = i
#
#    for z in range(int(count)):
#        elem = stacks[int(from_)].pop(0)
#        stacks[int(to_)].insert(0, elem)
#
##print(stacks)
#final =''
#for v in stacks.values():
#    final += v[0]
#
#print(final)
    
#############################################
# --- Part Two ---

for i in movement:
    count, from_, to_ = i

    elem = stacks[int(from_)][0:int(count)]
    stacks[int(from_)] = stacks[int(from_)][int(count):]
    stacks[int(to_)] = elem + stacks[int(to_)]

final =''
for v in stacks.values():
    final += v[0]

print(final)
