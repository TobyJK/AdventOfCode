f = open("8.txt")
firstPart, secondPart = [], []

for x in f:
    x = x[:-1]
    x = x.split(" | ")
    firstPart.append(x[1])
    secondPart.append(x[0])
count = 0
valid = [2, 3, 4, 7]
for digits in firstPart:
    digits = digits.split(" ")
    for num in digits:
        if len(num) in valid:
            count += 1
        
print("Part 1: {}".format(count))

for setOfDigits in secondPart:
    setOfDigits = setOfDigits.split(" ")
    completedDigits = ["", "", "", "", "", "", "", "", "", ""]
    for i in range(len(setOfDigits)):
        if len(setOfDigits[i]) == 2:
            completedDigits[i] = 1
            one = setOfDigits[i]
            inOne = list(setOfDigits[i])
        elif len(setOfDigits[i]) == 3:
            completedDigits[i] = 7
            seven = setOfDigits[i]
            inSeven = list(setOfDigits[i])
        elif len(setOfDigits[i]) == 4:
            completedDigits[i] = 4
            four = setOfDigits[i]
            inFour = list(setOfDigits[i])
        elif len(setOfDigits[i]) == 7:
            completedDigits[i] = 8
            eight = setOfDigits[i]
    twoThreeFive = [x for x in setOfDigits if len(x) == 5]
    zeroSixNine = [x for x in setOfDigits if len(x) == 6]
    a = str([x for x in inSeven if x not in inOne][0])
    bCheck = [list(x) for x in zeroSixNine]
    b = [x for x in inFour if x not in inOne]
    for posi in bCheck:
        for char in b:
            if char not in posi:
                d = char
                b.remove(char)
                zero = "".join(posi)
                i = setOfDigits.index(zero)
                completedDigits[i] = 0
    b = b[0]

    #Now, we have a,b,d, and correctly placed 0, 1, 4, 7 and 8 in the list
    done = [zero, one, four, seven, eight]
    remaining = [x for x in setOfDigits if x not in done] #2, 3, 5, 6, 9
    zeroSixNine.remove(zero)
    sixNine = zeroSixNine
    sixNineCheck = [list(x) for x in sixNine]
    twoThreeFiveCheck = [list(x) for x in twoThreeFive]
    for pos in twoThreeFiveCheck:
        pos = list(pos)
        check = [x for x in pos]
        pos = "".join(pos)
        try:
            check.remove(b)
            five = pos
            index = setOfDigits.index(five)
            completedDigits[index] = 5
            break
        except:
            next

    twoThreeFive.remove(five)
    twoThreeFiveCheck.remove(list(five))
    twoThree, twoThreeCheck = twoThreeFive, twoThreeFiveCheck
    for num in twoThreeCheck:
        num.remove(a)
        num.remove(d)
    cg = []
    ef = []
    for char in twoThreeCheck[0]:
        if char in twoThreeCheck[1]:
            cg.append(char)
        else:
            ef.append(char)
    for char in twoThreeCheck[1]:
        if char not in twoThreeCheck[0]:
            ef.append(char)
    
    for char in cg:
        if char in sixNineCheck[0] and sixNineCheck[1]:
            g = char
        else:
            c = char
    if c not in sixNineCheck[0]:
        six = "".join(sixNineCheck[0])
        nine = "".join(sixNineCheck[1])
    else:
        nine = "".join(sixNineCheck[0])
        six = "".join(sixNineCheck[1])
    index6, index9 = setOfDigits.index(six), setOfDigits.index(nine)
    completedDigits[index6], completedDigits[index9] = 6, 9
    
    nineCheck = list(nine)
    nineCheck.remove(a)
    nineCheck.remove(b)
    nineCheck.remove(c)
    nineCheck.remove(d)
    print(g, nineCheck)
    nineCheck.remove(g)
    print(nineCheck)