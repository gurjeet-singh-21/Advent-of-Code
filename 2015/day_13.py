#--- Day 13: Knights of the Dinner Table ---
#from itertools import permutations, combinations
#
#        +41 +46
#   +55   David    -2
#   Carol       Alice
#   +60    Bob    +54
#        -7  +83

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



n1 = list(names.copy())

collect = []
while len(n1):
    n = n1.pop()
    print(n, n1, len(n1))
    if len(n1) >= 1:
        temp = []
        for k, v in data.items():
            if (n == k[0]) and (k[1] in n1) and ('gain' in k):
                temp.append(v)
                print(temp)
            elif (n == k[0]) and (k[1] in n1) and ('lose' in k):
                temp.append(-v)
                print(temp)
        print('temp ', temp)
        collect.append(max(temp))
        print('collect ', collect)
    elif len(n1) == 0:
        for k, v in data.items():
            temp = []
            if (n == k[0]) and ('gain' in k):
                temp.append(v)
            elif (n == k[0]) and ('lose' in k):
                temp.append(-v)
        collect.append(max(temp))
print(collect)














#per = permutations(names)
#for i in per:
#    print(i)
#final = []
#collect = []
##while True:
##comb = combinations(names, 2)
#for i in per:
#    for j in data:
#        if i[0] in j and i[1] in j and 'gain' in j:
#            collect.append(data[j])
#        else:
#            if i[0] in j and i[1] in j and 'lose' in j:
#                collect.append(-data[j])
#print(len(collect))
