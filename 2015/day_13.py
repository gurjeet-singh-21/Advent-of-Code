#--- Day 13: Knights of the Dinner Table ---
from itertools import permutations, combinations
data = {}
names = set()
with open('/home/gurjeet/Desktop/in13.txt', 'r') as file:
#with open('input_13.txt' , 'r') as file:
    for i in file:
        j = i.split()
        for k in j:
            if k.isdigit():
                data[(j[0],j[-1][:-1],j[2])] = int(k)

for m in data:
    for n in m:
        if n not in ['lose','gain']:
            names.add(n)
per = permutations(names)
final = []
collect = []
#while True:
#comb = combinations(names, 2)
for i in per:
    for j in data:
        if i[0] in j and i[1] in j and 'gain' in j:
            collect.append(data[j])
        else:
            if i[0] in j and i[1] in j and 'lose' in j:
                collect.append(-data[j])
print(collect)
