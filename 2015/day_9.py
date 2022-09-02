#--- Day 9: All in a Single Night ---
#--- part one ---
from itertools import permutations

data = {}
cities = set()
with open('test_case_day_9.txt' ,'r') as file:
    for rows in file:
        key, value = rows.split(" = ")
        key = key.split(' to ')
        key = tuple(key)
        data[key] = int(value.strip())
    

for i in data:
    for j in i:
        cities.add(j)

final = []
per = permutations(cities)

for i in per:
    distance = 0
    for k,v in data.items():
        for j in range(len(i)-1):
            if i[j] in k and i[j+1] in k:
                distance += v
    final.append(distance)
#print(min(final))

#--- part two ---
print(max(final))
