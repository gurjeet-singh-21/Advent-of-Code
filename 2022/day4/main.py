# --- Day 4: Camp Cleanup ---

#with open('ex4.txt', 'r') as file:
with open('input4.txt', 'r') as file:
    data = [i.strip().split(",") for i in file]


new_data = [j.split("-") for i in data for j in i]

count = 0
l = len(new_data)

#for i in range(0, l, 2):
#
#    if int(new_data[i][0]) <= int(new_data[i+1][0]) and \
#            int(new_data[i][1]) >= int(new_data[i+1][1]):
#        count += 1
#
#    elif int(new_data[i][0]) >= int(new_data[i+1][0]) and \
#            int(new_data[i][1]) <= int(new_data[i+1][1]):
#        count += 1
#
#print(count)

# --- Part Two ---

for i in range(0, l, 2):

    if (int(new_data[i][0]) < int(new_data[i+1][0]) <= int(new_data[i+1][1])) and \
            (int(new_data[i][1]) < int(new_data[i+1][0]) <= int(new_data[i+1][1])):
        count += 1

    elif (int(new_data[i+1][0]) <= int(new_data[i+1][1]) < int(new_data[i][0])) and \
            (int(new_data[i+1][0]) <= int(new_data[i+1][1]) < int(new_data[i][1])):
        count += 1

print(l//2 - count)

