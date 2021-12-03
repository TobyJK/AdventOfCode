inputs = []
f = open("3.txt")
for x in f:
    wow = list(x)
    thing = []
    for char in wow:
        if char != "\n":
            thing.append(char)
    act = "".join(thing)
    inputs.append(act)
f.close()
myList = []
for i in range(len(inputs[0])):
    myList.append([0, 0])

for num in inputs:
    for i in range(len(num)):
        if num[i] == "1":
            myList[i][1] += 1
        else:
            myList[i][0] += 1

com = []
uncom = []

for bit in myList:
    if bit[0] > bit[1]:
        com.append(0)
        uncom.append(1)
    else:
        com.append(1)
        uncom.append(0)

comnum = int("".join(str(x) for x in com), 2)
uncomnum = int("".join(str(x) for x in uncom), 2)

print(comnum, uncomnum, comnum*uncomnum)

o2List = [x for x in inputs]
co2List = [x for x in inputs]
o2 = []
co2 = []
i = 0

while True:
    if len(o2List) > 1 or len(co2List) > 1:
        o2Val, co2Val = 0, 0
        temp = [0, 0]
        for ox in o2List:
            if ox[i] == "0":
                temp[0] += 1
            else:
                temp[1] += 1
        if temp[0] > temp[1]:
            o2Val = "0"
        else:
            o2Val = "1"
        temp = [0, 0]
        for co in co2List:
            if co[i] == "0":
                temp[0] += 1
            else:
                temp[1] += 1
        if temp[0] > temp[1]:
            co2Val = "1"
        else:
            co2Val = "0"

        if len(o2List) > 1:
            o2 = [x for x in o2List if x[i] == o2Val]
        if len(co2List) > 1:
            co2 = [x for x in co2List if x[i] == co2Val]
        
        o2List = [x for x in o2]
        co2List = [x for x in co2]
    else:
        break
    i += 1

o2, co2 = list(o2), list(co2)

o2num = int("".join(str(x) for x in o2), 2)
co2num = int("".join(str(x) for x in co2), 2)

print(o2num, co2num, o2num*co2num)