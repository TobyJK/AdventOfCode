inputs = []
f = open("2.txt")
for x in f:
    wow = list(x)
    thing = []
    for char in wow:
        if char != "\n":
            thing.append(char)
    act = "".join(thing)
    inputs.append(act)
f.close()

horizontal, depth = 0, 0
for thing in inputs:
    if thing[0] == "f":
        horizontal += int(thing[-1])
    elif thing[0] == "d":
        depth += int(thing[-1])
    else:
        depth -= int(thing[-1])
print(horizontal, depth, horizontal*depth)

horizontal, depth, aim = 0, 0, 0
for thing in inputs:
    if thing[0] == "f":
        horizontal += int(thing[-1])
        depth += int(thing[-1]) * aim
    elif thing[0] == "d":
        aim += int(thing[-1])
    else:
        aim -= int(thing[-1])
print(horizontal, depth, aim, horizontal*depth)