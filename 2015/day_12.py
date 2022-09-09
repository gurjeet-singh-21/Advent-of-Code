#--- Day 12: JSAbacusFramework.io ---

# get the entire data as dictionary in a variable <data>

import json
with open("input_12.txt", 'r') as file:
    input = file.read()
data = json.loads(input)
sum = 0
# --- part one ---
# crearting a recursive function
#def rec_json(d):
#    # check if arg is dict, then take the value and recurse
#    if isinstance(d, dict):
#        for v1 in d.values():
#            yield from rec_json(v1)
#    # check if arg is list, then using for loop extract each element and recurse
#    elif isinstance(d, list):
#        for k2 in d:
#            yield from rec_json(k2)
#    # check if int, get that out to a list
#    elif isinstance(d, int):
#        yield d
##print(list(rec_json(data)))
#d1 = list(rec_json(data))
#for i in d1:
#    sum += i
#print(sum)

# --- part two ---

def rec_json(d):

    if isinstance(d, dict):
        for v1 in d.values():
            if type(v1) not in [int, str, list] and('red' in v1.keys() or 'red' in
                    v1.values()):
                yield 0
            else:
                yield from rec_json(v1)
    elif isinstance(d, list):
        for k2 in d:
            yield from rec_json(k2)
    elif isinstance(d, int):
        yield d
d1 = list(rec_json(data))
for i in d1:
    sum += i
print(sum)
