import sys
input = sys.stdin.readline

def checkCol(x, n):
    for i in range(9):
        if board[x][i] == n:
            return False
    return True

def checkRow(y, n):
    for i in range(9):
        if board[i][y] == n:
            return False
    return True

def checkBlock(x, y, n):
    cx = x//3 * 3
    cy = y//3 * 3
    for i in range(cx, cx+3):
        for j in range(cy, cy+3):
            if board[i][j] == n:
                return False
    return True

def dfs(idx):
    global length
    if idx == length:
        for i in range(9):
            print(*board[i], sep="")
        exit()
    x, y = blank[idx]
    for i in range(10):
        if checkCol(x, i) and checkRow(y, i) and checkBlock(x, y, i):
            board[x][y] = i
            dfs(idx+1)
            board[x][y] = 0
    return


board = [list(map(int, input().split())) for _ in range(9)]
blank = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]
length = len(blank)

dfs(0)