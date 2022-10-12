boards = []
f = open("4.txt")

x = f.readline()
x = x[:-1]
calls = x.split(",")
board = []

for x in f:
    if x != "\n":
        x = x[:-1]
        line = x.split(" ")
        for _ in range(3):
            try:
                line.remove(" ")
            except:
                a = 1
            try:
                line.remove("\n")
            except:
                a = 1
            try:
                line.remove("")
            except:
                a = 1
        board.append(line)
    else:
        if board:
            boards.append(board)
        board = []

def check(board):
    for row in board:
        no = False
        for num in row:
            if type(num) is str:
                no = True
                break
        if no == False:
            return True
    for i in range(5):
        no = False
        for row in board:
            if type(row[i]) is str:
                no = True
                break
        if no == False:
            return True
    return False

def score(board, call):
    sum = 0
    for row in board:
        for num in row:
            if type(num) is str:
                sum += int(num)
    return sum*int(call)

count = 0
for nu in calls:
    for boar in boards:
        for row in boar:
            if nu in row:
                index = row.index(nu)
                row[index] = int(nu)
        if check(boar) == True:
            boards.remove(boar)
            lastBoard = boar
            lastCall = nu
            if count == 0 or len(boards) == 0:
                print(score(boar, nu))
            count += 1