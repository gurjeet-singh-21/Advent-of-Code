##########################################
#--- Day 6: Probably a Fire Hazard ---
#--- part one ---

#For example:
#
#    turn on 0,0 through 999,999 would turn on (or leave on) every light.
#    toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
#    turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
#
#After following the instructions, how many lights are lit?
##########################################
light = {(i,j):False for i in range(1000) for j in range(1000)}
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
                    if light[(i,j)]:
                        light[(i,j)] = False
                    else:
                        light[(i,j)] = True

                elif row[0]=='turn'and row[1]=='on':
                    light[(i,j)] = True

                elif row[0]=='turn'and row[1]=='off':
                    light[(i,j)] = False

    for k in light.values():
        if k:
            total += 1
    print(total)

