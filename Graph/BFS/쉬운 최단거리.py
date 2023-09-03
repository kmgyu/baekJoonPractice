import sys
from collections import deque
input = sys.stdin.readline

def solve():
    q = deque()
    x, y = -1, -1
    for i in range(n):
        for j in range(m):
            if mat[i][j]==2:
                x = i
                y = j
                break
        if x >= 0 and y >= 0: break
    
    q.append((x, y))
    distance[x][y] = 0
    while q:
        a, b = q.popleft()
        for i in range(4):
            mx = a+dx[i]
            my = b+dy[i]
            if mx < 0 or mx >= n or my < 0 or my >= m: continue
            if distance[mx][my] == -1:
                if mat[mx][my] == 0:
                    distance[mx][my] = 0; continue
                distance[mx][my] = distance[a][b]+1
                q.append((mx, my))
    
    for i in range(n):
        for j in range(m):
            if distance[i][j] == -1 and mat[i][j] == 0:
                distance[i][j] = 0

dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

n, m = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(n)]
distance = [[-1] * m for _ in range(n)]
solve()
for i in distance:
    print(*i)