##########################
#--- Day 3: Perfectly Spherical Houses in a Vacuum ---
# --- part one ---
#For example:
#
#    > delivers presents to 2 houses: one at the starting location, and one to the east.
#    ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
#    ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
###########################
#x = 0
#y = 0
#with open('test_case_day_3.txt', 'r') as file:
#    houses = [(0,0)]
#
#    for items in file:
#        for data in items:
#            if data == '<' or data == '>':
#                if data == '>':
#                    x += 1
#                elif data == '<':
#                    x -= 1
#            
#            elif data == '^' or data == 'v':
#                if data == '^':
#                    y += 1
#                elif data == 'v':
#                    y -= 1
#
#
#            if (x,y) not in houses:
#                houses.append((x,y))
#            else:
#                continue
#    print(len(houses))
#############################################
#--- Part Two ---
#For example:
#
#    ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
#    ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
#    ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
#############################################

with open('test_case_day_3.txt', 'r') as file:
    for x in file:
        h1 = {(0,0)}
        h2 = {(0,0)}
        h = set()
        c1 = 0 ; c2= 0; c3 = 0;c4=0
        for i in range(0,len(x),2):
            if x[i] == '>':
                c1 += 1
            elif x[i] == '<':
                c1 -= 1
            elif x[i] == '^':
                c2 += 1
            elif x[i] == 'v':
                c2 -= 1

            h1.add((c1,c2))

        for j in range(1,len(x),2):
            if x[j] == '>':
                c3 += 1
            elif x[j] == '<':
                c3 -= 1
            elif x[j] == '^':
                c4 += 1
            elif x[j] == 'v':
                c4 -= 1

            h2.add((c3,c4))
    h =  h1.union(h2)
    print(len(h))
