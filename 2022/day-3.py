# --- Day 3: Rucksack Reorganization ---

import string


strings = string.ascii_lowercase + string.ascii_uppercase

total = 0

#with open('ex3.txt', 'r') as file:
with open('input3.txt', 'r') as file:
    data = [i.strip() for i in file]

#for i in data:
#    l = len(i)
#    first = i[:l//2]
#    second = i[l//2:]
#
#    for i, j in enumerate(strings):
#        if j in first and j in second:
#            total += i + 1
#
#print(total)
temp = 0

# --- Part Two ---
while len(data) > temp:

    for index, badge in enumerate(strings):
        if badge in data[temp] and badge in data[temp+1] and badge in data[temp+2]:
            total += index + 1

    temp += 3

print(total)

