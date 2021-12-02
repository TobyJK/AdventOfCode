inputs = []
f = open("1.txt")
for x in f:
    wow = list(x)
    thing = []
    for char in wow:
        if char != "\n":
            thing.append(char)
    act = "".join(thing)
    inputs.append(int(act))
f.close()

start = 100000000
count = 0
for x in inputs:
    if x > start:
        count += 1
    start = x
print(count)

length = len(inputs)
length -= 1
groups = []
for i in range(length-1):
    first = inputs[i]
    second = inputs[i+1]
    third = inputs[i+2]
    group = [first, second, third]
    groups.append(group)

first = 100000000
count = 0
for group in groups:
    add = sum(group)
    if add > first:
        count += 1
    first = add
print(count)