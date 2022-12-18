import re
with open("5.txt") as f:
    l, c, d = [], [], []
    for _ in range(8):
        l.append(f.readline()[:-1])
    key = f.readline()[:-1]
    for i in range(1, 10):
        this = []
        ind = key.index(str(i))
        for line in l:
            if line[ind] != " ":
                this.append(line[ind])
        c.append(this)
        d.append(this.copy())
    f.readline()
    for line in f.readlines():
        op = [int(x[1:-1]) for x in re.findall(" [0-9]+[ \n]", line)]
        t = []
        for _ in range(op[0]):
            c[op[2]-1].insert(0, c[op[1]-1].pop(0))
            t.insert(0, d[op[1]-1].pop(0))
        for thing in t:
            d[op[2]-1].insert(0, thing)

print("".join([x[0] for x in c]))
print("".join([x[0] for x in d]))