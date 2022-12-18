c1, c2 = 0, 0
with open("4.txt") as f:
    for line in f:
        t = [int(x) for x in sum([x.split("-") for x in line.strip().split(",")], [])]
        if (t[0] >= t[2] and t[1] <= t[3]) or (t[2] >= t[0] and t[3] <= t[1]):
            c1 += 1
        if (t[0] < t[3] and t[1] < t[2]) or (t[3] < t[0] and t[2] < t[1]):
            print(line)
            c2 += 1
print(c1, 1000-c2)