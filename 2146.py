from collections import deque
import sys
sys.setrecursionlimit(10**5)

def dfs(x, y): #island counter
    global cnt
    if graph[x][y] == 1:
        graph[x][y] += cnt
    else: return
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if mx < 0 or my < 0 or mx >= n or my >= n: continue
        if graph[mx][my] == 1:
            dfs(mx, my)

answer = 10e9
def bfs(color):
    global answer
    dist = [[-1] * (n) for _ in range(n)]
    q = deque()
    
    for i in range(n):
        for j in range(n):
            if graph[i][j] == color:
                q.append([i, j])
                dist[i][j] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if mx < 0 or my < 0 or mx >= n or my >= n: continue
            if graph[mx][my] != color and graph[mx][my] > 0:
                answer = min(answer, dist[x][y])
                return
            if graph[mx][my] == 0 and dist[mx][my] == -1:
                dist[mx][my] = dist[x][y] + 1
                q.append([mx, my])

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

cnt = 0
for i in range(n): #섬 구분시키기
    for j in range(n):
        if graph[i][j] == 1: cnt += 1
        dfs(i, j)
for i in range(2, cnt+1):
    bfs(i)
print(answer)