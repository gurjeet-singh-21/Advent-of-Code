#--- Day 9: All in a Single Night ---
#--- part one ---
import random
data = {}

with open('/home/gurjeet/Desktop/testCase.txt', 'r') as file:
    for i in file:
        key, value = i.strip().split("=")
        data[key.strip()] = int(value)

cities = set()
for i in data:
    i = i.split()
    cities.add(i[0])
    cities.add(i[-1])

# example - 
# London = 0
# London to Dublin = 464
# Dublin to Belfast = 141

# take 1 city at random, start with 0 and then search for next city from there

#city = random.choice(list(cities))
for city in cities:
    d = 0
    next_city = random.choice(list(cities))
    if 
