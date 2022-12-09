# --- Day 1: Calorie Counting ---

elfs = {}
energy = 0
total = []

#with open('ex1.txt', 'r') as file:
with  open('input1.txt', 'r') as file:
    data = [i.strip() for i in file]

for i in data:
    if i:
        energy += int(i)

    else:
        total.append(energy)
        energy = 0
total.append(energy)

#print(max(total))

# --- Part Two --- Total calories carried by top 3 Elfs
top_three = []
for j in range(3):
    top_three.append(total.pop(total.index(max(total))))
print(sum(top_three))

