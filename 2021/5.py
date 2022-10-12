inputs = []
f = open("5.txt")
for x in f:
    x = x[:-1]
    x = x.split(" -> ")
    thing = []
    for item in x:
        item = item.split(",")
        for l in item:
            thing.append(int(l))
    inputs.append(thing)

grid = []
for _ in range(1000):
    thing = []
    for _ in range(1000):
        thing.append(0)
    grid.append(thing)

p1easy = [x for x in inputs if x[0] == x[2]]
p1hard = [x for x in inputs if x[1] == x[3]]

for coord in p1easy:
    row = coord[0]
    coord = [x for x in coord if x != row]
    if coord[0] > coord[1]:
        large, small = coord[0], coord[1]
    else:
        small, large = coord[0], coord[1]
    for i in range(small, large+1):
        grid[row][i] += 1

for coord in p1hard:
    column = coord[1]
    coord = [x for x in coord if x != column]
    if coord[0] > coord[1]:
        large, small = coord[0], coord[1]
    else:
        small, large = coord[0], coord[1]
    for i in range(small, large+1):
        grid[i][column] += 1

count = 0
for row in grid:
    for thing in row:
        if thing > 1:
            count += 1

print("Part 1: {}".format(count))

p2 = [x for x in inputs if x[0] != x[2] and x[1] != x[3]]

for coord in p2:
    if coord[2] > coord[0] and coord[3] > coord[1]:
        for x, y in zip(range(coord[0], coord[2] + 1), range(coord[1], coord[3] + 1)):
            grid[x][y] += 1
    elif coord[0] > coord[2] and coord[3] > coord[1]:
        for x, y in zip(range(coord[0], coord[2] - 1, -1), range(coord[1], coord[3] + 1)):
            grid[x][y] += 1
    elif coord[2] > coord[0] and coord[1] > coord[3]:
        for x, y in zip(range(coord[0], coord[2] +1), range(coord[1], coord[3] - 1, -1)):
            grid[x][y] += 1
    else:
        for x, y in zip(range(coord[0], coord[2] - 1, -1), range(coord[1], coord[3] - 1, -1)):
            grid[x][y] += 1

count = 0
for row in grid:
    for thing in row:
        if thing > 1:
            count += 1

print("Part 2: {}".format(count))