f = open("1.txt")
this = 0
that = []
for line in f:
    if line.strip():
        this += int(line)
    else:
        that.append(this)
        this = 0

that.sort()
print(that[-1])
print(sum(that[-3:]))