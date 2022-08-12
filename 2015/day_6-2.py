#################################################
#--- Part Two ---
#
#What is the total brightness of all lights combined after following Santa's instructions?
#
#For example:
#
#    turn on 0,0 through 0,0 would increase the total brightness by 1.
#    toggle 0,0 through 999,999 would increase the total brightness by 2000000.
#################################################

light = {(i,j):0 for i in range(1000) for j in range(1000)}
total = 0
with open('test_case_day_6.txt', 'r') as file:
    for rows in file:
        row = rows[:-1].split(' ')
        data = [i for i in row if ',' in i]
        data = ','.join(data)
        data = data.split(',')
        
        for i in range(int(data[0]), int(data[2])+1):
            for j in range(int(data[1]), int(data[3])+1):

                if row[0] == 'toggle':
                    light[(i,j)] += 2

                elif row[0]=='turn'and row[1]=='on':
                    light[(i,j)] += 1

                elif row[0]=='turn'and row[1]=='off':
                    light[(i,j)] -= 1
                    if light[(i,j)] < 0:
                        light[(i,j)] = 0
    for k in light.values():
        total += k
    print(total)

