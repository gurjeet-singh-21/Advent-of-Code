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
with open('test_case_day_7.txt', 'r') as file:
    for rows in file:
        value, key = rows.split("-> ")
        data[key.strip()] = value.strip()

for _ in data:
    if data[_].isdigit():
        data[_] = int(data[_])
    else:
        data[_] = data[_].split()

for i in data:
    if 'NOT' in data[i]:
        data[i] = ~data[i][-1] & 0xffff
print(data)
#    else:
#    if data[1] == 'AND':
#        final[data[-1]] = final[data[0]] & final[data[2]]
#
#    elif data[1] == 'OR':
#        final[data[-1]] = final[data[0]] | final[data[2]]
#
#    elif data[1] == 'LSHIFT':
#        final[data[-1]] = final[data[0]] << int(data[2])
#
#    elif data[1] == 'RSHIFT':
#        final[data[-1]] = final[data[0]] >> int(data[2])
#print(final['a'])
