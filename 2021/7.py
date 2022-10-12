from os import stat
import statistics
inputs = [int(x) for x in open("7.txt").read().strip().split(",")]
inputs.sort()
input1 = inputs[:-1]
input2 = inputs[1:]

values = [statistics.median(input1), statistics.median(input2)]
total1, total2 = 0, 0

for x in inputs:
    total1 += abs(x - values[0])
    total2 += abs(x - values[1])

print(total1, total2)

values = [int(statistics.mean(inputs)), int(statistics.mean(inputs))]
total1, total2 = 0, 0

for x in inputs:
    dif1 = abs(x - values[0]) + 1
    dif2 = abs(x - values[1]) + 1

    for x in range(1, dif1):
        total1 += x
    for x in range(1, dif2):
        total2 += x

print(total1, total2)