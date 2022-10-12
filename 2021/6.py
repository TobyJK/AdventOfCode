f = open("6.txt")
x = f.read()
inputs = x.split(",")
f.close()
fish = {}
for i in range(9):
    fish[i] = 0

for x in inputs:
    fish[int(x)] += 1

for _ in range(80):
    copy = {}
    for x in fish:
        copy[x] = fish[x]
    
    copy[8] = fish[0]
    copy[7] = fish[8]
    copy[6] = fish[7] + fish[0]
    copy[5] = fish[6]
    copy[4] = fish[5]
    copy[3] = fish[4]
    copy[2] = fish[3]
    copy[1] = fish[2]
    copy[0] = fish[1]

    for x in copy:
        fish[x] = copy[x]

total = 0
for x in fish:
    total += fish[x]

print("Part 1: {}".format(total))

for i in range(9):
    fish[i] = 0

for x in inputs:
    fish[int(x)] += 1

for _ in range(256):
    copy = {}
    for x in fish:
        copy[x] = fish[x]
    
    copy[8] = fish[0]
    copy[7] = fish[8]
    copy[6] = fish[7] + fish[0]
    copy[5] = fish[6]
    copy[4] = fish[5]
    copy[3] = fish[4]
    copy[2] = fish[3]
    copy[1] = fish[2]
    copy[0] = fish[1]

    for x in copy:
        fish[x] = copy[x]

total = 0
for x in fish:
    total += fish[x]

print("Part 2: {}".format(total))