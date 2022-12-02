res1 = {
    "X" : {"A" : 3, "B" : 0, "C" : 6, "s" : 1},
    "Y" : {"A" : 6, "B" : 3, "C" : 0, "s" : 2},
    "Z" : {"A" : 0, "B" : 6, "C" : 3, "s" : 3}
}
res2 = {
    "X" : {"A" : 3, "B" : 1, "C" : 2, "s" : 0},
    "Y" : {"A" : 1, "B" : 2, "C" : 3, "s" : 3},
    "Z" : {"A" : 2, "B" : 3, "C" : 1, "s" : 6}
}
t1 = 0
t2 = 0
with open("2.txt") as f:
    for line in f:
        t1 += res1[line.strip()[2]]["s"] + res1[line.strip()[2]][line.strip()[0]]
        t2 += res2[line.strip()[2]]["s"] + res2[line.strip()[2]][line.strip()[0]]
print(t1)
print(t2)