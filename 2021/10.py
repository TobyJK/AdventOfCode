import statistics

inputs = []
f = open("10.txt")
for x in f:
    x = x[:-1]
    inputs.append(list(x))

opening, closing, scores1, scores2 = ["(", "[", "{", "<"], [")", "]", "}", ">"], [3, 57, 1197, 25137], [1, 2, 3, 4]
part2 = [x for x in inputs]

score = 0
for x in inputs:
    corrupted = False
    stack = []
    for brack in x:
        if brack in opening:
            stack.append(brack)
        else:
            pos = closing.index(brack)
            if stack[-1:][0] == opening[pos]:
                stack.pop()
            else:
                score += scores1[pos]
                corrupted = True
        if corrupted == True:
            part2.remove(x)
            break
print("Part 1: {}".format(score))

scores = []
for x in part2:
    score = 0
    stack = []
    for brack in x:
        if brack in opening:
            stack.append(brack)
        else:
            pos = closing.index(brack)
            if stack[-1:][0] == opening[pos]:
                stack.pop()
    stack.reverse()
    for brack in stack:
        pos = opening.index(brack)
        score *= 5
        score += scores2[pos]
    scores.append(score)

print("Part 2: {}".format(statistics.median(scores)))