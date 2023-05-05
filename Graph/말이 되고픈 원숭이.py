from collections import deque
from sys import stdin
#reference
# https://www.acmicpc.net/board/view/18927
input = stdin.readline
dx = [1, -1, 0, 0, 2, 2, 1, -1, -2, -2, 1, -1]
dy = [0, 0, 1, -1, 1, -1, 2, 2, 1, -1, -2, -2]
def bfs(k):
    que = deque()
    que.append([0, 0, k])
    while que:
        x, y, km = que.popleft()
        if x == m-1 and y == n-1:
            print(d[x][y][km])
            return
        for i in range(12):
            nx = x+dx[i]
            ny = y+dy[i]
            if i >= 4 and km == 0: break
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if i < 4:
                if board[nx][ny] == 0 and d[nx][ny][km] == 0:
                    d[nx][ny][km] = d[x][y][km]+1
                    que.append([nx,ny,km])
            else: #knight move
                if board[nx][ny] == 0 and d[nx][ny][km-1] == 0:
                    d[nx][ny][km-1] = d[x][y][km] + 1
                    que.append([nx,ny,km-1])
    print(-1)
k = int(input())  # knight move
n, m = map(int,input().split())
board = [[0] * n for _ in range(m)]
d = [[[0] * (k+1) for _ in range(n)] for _ in range(m)]
for i in range(m):
    temp = list(map(int, input().split()))
    for j in range(n):
        board[i][j] = temp[j]
bfs(k)