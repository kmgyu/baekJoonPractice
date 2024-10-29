from collections import deque
from sys import stdin
input = stdin.readline

dx = [2, 2, 1, -1, -2, -2, 1, -1]
dy = [1, -1, 2, 2, 1, -1, -2, -2]

def bfs(a, b):
    que = deque()
    que.append([a, b])
    while que:
        x, y = que.popleft()
        for i in range(8):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if board[nx][ny] == 0:
                board[nx][ny] = board[x][y]+1
                que.append([nx,ny])
            elif board[nx][ny] == -1:
                print(board[x][y])
                return

for i in range(int(input())):
    n = int(input())
    board = [[0] * n for _ in range(n)]
    a, b = map(int, input().split())
    board[a][b] = 1 #나이트 현재칸
    c, d = map(int, input().split())
    board[c][d] = -1 #도착지점
    bfs(a,b)




