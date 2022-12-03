t1, t2, g = 0, 0, []
with open("3.txt") as f:
    for line in f:
        line = line.strip()
        if len(g) < 2:
            g.append(line)
        else:
            g.append(line)
            d = [dict.fromkeys(x) for x in g]
            for i in d[0]:
                if i in d[1] and i in d[2]:
                    if i.upper() == i:
                        t2 += ord(i) - 38
                    else:
                        t2 += ord(i) - 96
            g = []

        l1 = dict.fromkeys(line[:len(line)//2])
        l2 = dict.fromkeys(line[len(line)//2:])
        for i in l1:
            if i in l2:
                if i.upper() == i:
                    t1 += ord(i) - 38
                else:
                    t1 += ord(i) - 96
print(t1)
print(t2)