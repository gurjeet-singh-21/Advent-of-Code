# --- Day 1: Sonar Sweep ---

count = 0
data = []
with open('input-1.txt', 'r') as file:
    for i in file:
        data.append(int(i.strip()))

depth = data[0]

for item in data[1:]:
    if depth < item:
        depth = item
        count += 1
    else:
        depth = item
print(count) 
