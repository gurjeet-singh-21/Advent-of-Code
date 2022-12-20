# --- Day 8: Treetop Tree House ---

with open("input8.txt", 'r') as file:
#with open("ex8.txt", 'r') as file:
    data = [i.strip() for i in file]
lines= []
for i in data:
    lines.append([int(j) for j in i])

row = len(lines)
column = len(lines[0])
count = row*2 + column*2 - 4

for i in range(1, row-1):
    for j in range(1, column-1):
        x=0; y=0;
        temp_x, temp_y = 0, 0
        while x < row:
            if x < i:
                if lines[i][j] <= lines[x][j]:
                    temp_x += 1
                    x = i + 1
                else:
                    x += 1
            elif x > i:
                if lines[i][j] <= lines[x][j]:
                    temp_x += 1
                    x = row
                else:
                    x += 1
            else:
                x += 1
                continue

        while y < column:
            if y < j:
                if lines[i][j] <= lines[i][y]:
                    temp_y += 1
                    y = j + 1
                else:
                    y += 1

            elif y > j:
                if lines[i][j] <= lines[i][y]:
                    temp_y += 1
                    y = column
                else:
                    y += 1
            else:
                y += 1
                continue
        if temp_x + temp_y < 4:
            count += 1
print("part1=", count)
