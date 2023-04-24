from collections import deque
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
graph = [[False] * (m+2) for _ in range(n+2)]  # padding
visited = [[False] * (m+2) for _ in range(n+2)]
distance = [[0] * (m+2) for _ in range(n+2)]
for i in range(n):
    li = list(input())
    for j in range(m):
        if li[j] == '1':
            graph[i+1][j+1] = True

def bfs(x, y):
    visited[x][y] = True
    que = deque([[x, y]])
    while que:
        coor = que.popleft()
        x = coor[0]
        y = coor[1]
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            if graph[next_x][next_y] and (not visited[next_x][next_y]):
                distance[next_x][next_y] = distance[x][y]+1
                visited[next_x][next_y] = True
                que.append([next_x, next_y])

bfs(1,1)
print(distance[n][m]+1)