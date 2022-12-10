# --- Day 6: Tuning Trouble ---

#with open('ex6.txt', 'r') as file:
with open('input6.txt', 'r') as file:
    data = [i.strip() for i in file]

#def marker(strings):
#    count = 0
#    for i in range(len(strings)):
#        if len(set(strings[i:i+4])) == 4:
#            count = i + 4
#            return count

# --- Part Two ---

def marker(strings):
    count = 0
    for i in range(len(strings)):
        if len(set(strings[i:i+14])) == 14:
            count = i + 14
            return count

for item in data:
    print(marker(item))
