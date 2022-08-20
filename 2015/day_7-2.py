########################
#--- Part Two ---
#
#Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
########################


data = dict()
d1 = dict()
d2 = dict()

with open('test_case_day_7.txt', 'r') as file:
    for rows in file:
        value, key = rows.split("-> ")
        data[key.strip()] = value.strip()

for _ in data:
    if data[_].isdigit():
        d1[_] = int(data[_])
    else:
        d2[_] = data[_].split()

def signal(d1,d2,data):

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
    return d1['a']
d3 = {}
for _ in data:
    if data[_].isdigit():
        d3[_] = int(data[_])
    else:
        d2[_] = data[_].split()

d3['b'] = signal(d1,d2,data)

print(signal(d3,d2,data))
