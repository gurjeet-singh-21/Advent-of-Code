########################################
#--- Day 7: Some Assembly Required ---
#
#For example:
#
#    123 -> x means that the signal 123 is provided to wire x.
#    x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
#    p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
#    NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
#
#Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.
#
#For example, here is a simple circuit:
#
#123 -> x
#456 -> y
#x AND y -> d
#x OR y -> e
#x LSHIFT 2 -> f
#y RSHIFT 2 -> g
#NOT x -> h
#NOT y -> i
#
#After it is run, these are the signals on the wires:
#
#d: 72
#e: 507
#f: 492
#g: 114
#h: 65412
#i: 65079
#x: 123
#y: 456
#
#In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
#############################################

data = dict()
d1 = dict()
d2 = dict()

#with open('test_case_day_7.txt', 'r') as file:
with open('test_case_day_7.txt', 'r') as file:
    for rows in file:
        value, key = rows.split("-> ")
        data[key.strip()] = value.strip()

for _ in data:
    if data[_].isdigit():
        d1[_] = int(data[_])
    else:
        d2[_] = data[_].split()

while len(d1) != len(data):
    for i in d2:
        
        if 'AND' in d2[i]:
            if d2[i][0].isdigit() and d2[i][-1] in d1:
                d1[i] = int(d2[i][0]) & d1[d2[i][-1]]
             
            elif d2[i][-1].isdigit() and d2[i][0] in d1:
                d1[i] = d1[d2[i][0]] & int(d2[i][-1])

            elif d2[i][0] in d1 and d2[i][-1] in d1:
                d1[i] = d1[d2[i][0]] & d1[d2[i][-1]]


        elif 'OR' in d2[i]:
            if d2[i][0].isdigit() and d2[i][-1] in d1:
                d1[i] = int(d2[i][0]) | d1[d2[i][-1]]
             
            elif d2[i][-1].isdigit() and d2[i][0] in d1:
                d1[i] = d1[d2[i][0]] | int(d2[i][-1])

            elif d2[i][0] in d1 and d2[i][-1] in d1:
                d1[i] = d1[d2[i][0]] | d1[d2[i][-1]]


        elif d2[i][-1] in d1 and 'NOT' in d2[i]:
            d1[i] = ~d1[d2[i][-1]] & 0xffff

        elif d2[i][0] in d1:
            if 'LSHIFT' in d2[i]:
                d1[i] = d1[d2[i][0]] << int(d2[i][-1])

            elif 'RSHIFT' in d2[i]:
                d1[i] = d1[d2[i][0]] >> int(d2[i][-1])

            else:
                d1[i] = d1[d2[i][0]]

print(d1['a'])
