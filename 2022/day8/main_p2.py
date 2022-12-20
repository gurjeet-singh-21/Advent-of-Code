# --- Day 8: Treetop Tree House ---
# --- Part Two ---

lines = []
with open("input8.txt", 'r') as file:
#with open("ex8.txt", 'r') as file:
    data = [i.strip() for i in file]

for i in data:
    lines.append([int(j) for j in i])

row = len(lines)
column = len(lines[0])
view = []

for i in range(1, row-1):
    for j in range(1, column-1):
        left = right = up = down = 0

        for a in range(i-1, -1, -1):
            up += 1
            if lines[i][j] <= lines[a][j]:
                break

        for b in range(i+1, row):
            down += 1
            if lines[i][j] <= lines[b][j]:
                break

        for c in range(j-1, -1, -1):
            left += 1
            if lines[i][j] <= lines[i][c]:
                break

        for d in range(j+1, column):
            right += 1
            if lines[i][j] <= lines[i][d]:
                break

        view.append(left * right * up * down)

print("part2 = ", max(view))
