import sys
sys.setrecursionlimit(10**6)
t = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    if visited[x][y]:return
    visited[x][y] = True
    for i in range(4):
        mx = x+dx[i]
        my = y+dy[i]
        if mx>=n or my>=m or mx < 0 or my < 0: continue
        if graph[mx][my] == 1 and not visited[mx][my]:
            dfs(mx,my)

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    cnt = 0
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)