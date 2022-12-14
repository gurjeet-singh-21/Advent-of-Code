# --- Day 7: No Space Left On Device ---

from collections import defaultdict

#with open("ex7.txt", 'r') as file:
with open("input7.txt", 'r') as file:
#with open("test.txt", 'r') as file:
    data = [i.split() for i in file]

path = []
fullpath = defaultdict(int)

for line in data:
    if line[1] == 'cd':
        if line[2] == '..':
            path.pop()
        else:
            path.append(line[-1])
    elif line[1] == 'ls':
        continue
    elif line[0] == 'dir':
        continue
    else:
        size = int(line[0])
        for i in range(1,len(path)+1):
            fullpath["/".join(path[:i])] += size

#print(sum(i for i in fullpath.values() if i <= 100000))

# --- Part Two ---

#print(max(fullpath.values()))
total_disk_space = 70000000
min_space = 30000000
temp = [i for i in fullpath.values()]
difference = total_disk_space - min_space
used_spaces = temp.pop(temp.index(max(temp)))
j = []
for i in temp:
    # space left + files removed should be >= minimum space requirement
    if (total_disk_space - used_spaces + i) >= min_space:
        j.append(i)
print(min(j))
        
