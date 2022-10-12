import numpy

f = open("9.txt")
inputs = []
for x in f:
    x = x[:-1]
    thing = list(x)
    x = [int(x) for x in thing]
    inputs.append(x)

def getNeighbours1(x, y):
    neighbours = []
    if x != 0:
        neighbours.append(inputs[y][x-1])
    if x != len(inputs[y])-1:
        neighbours.append(inputs[y][x+1])
    if y != 0:
        neighbours.append(inputs[y-1][x])
    if y != len(inputs)-1:
        neighbours.append(inputs[y+1][x])
    return neighbours

score = 0
part2 = [x for x in inputs]
lowPoints = []

for a in range(len(inputs)):
    for b in range(len(inputs[a])):
        part2[a][b] = inputs[a][b]
        vals = getNeighbours1(b, a)
        check = len(vals)
        count = 0
        for val in vals:
            if inputs[a][b] < val:
                count += 1
        if count == check:
            score += inputs[a][b] + 1
            lowPoints.append([a, b])

print("Part 1: {}".format(score))

def getNeighbours2(x, y):
    toVisit = []
    if x != 0:
        if part2[y][x-1] != -1 and part2[y][x-1] != 9:
            part2[y][x-1] = -1
            toVisit.append([x-1, y])
    if x != len(part2[y])-1:
        if part2[y][x+1] != -1 and part2[y][x+1] != 9:
            part2[y][x+1] = -1
            toVisit.append([x+1, y])
    if y != 0:
        if part2[y-1][x] != -1 and part2[y-1][x] != 9:
            part2[y-1][x] = -1
            toVisit.append([x, y-1])
    if y != len(part2)-1:
        if part2[y+1][x] != -1 and part2[y+1][x] != 9:
            part2[y+1][x] = -1
            toVisit.append([x, y+1])
    return toVisit

def basin(a, b):
    visits = []
    toDo = getNeighbours2(b, a)
    m = 0
    while True:
        for u in toDo:
            visits.append(u)
        try:
            toDo = getNeighbours2(visits[m][0], visits[m][1])
        except:
            size = len(visits)
            return size
        m += 1

basins = []

for low in lowPoints:
    thing = basin(low[0], low[1])
    basins.append(thing)

basins.sort()
print("Part 2: {}".format(numpy.prod(basins[-3:])))