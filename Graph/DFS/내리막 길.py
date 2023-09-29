import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(a, b):
    if a == n-1 and b == m-1:
        return 1
    if visited[a][b] != -1 : return visited[a][b]
    
    visited[a][b] = 0
    for i in range(4):
        mx = a+dx[i]
        my = b+dy[i]
        if mx < 0 or mx >= n or my < 0 or my >= m: continue
        if mat[mx][my] >= mat[a][b]: continue
        visited[a][b] += dfs(mx, my)
    return visited[a][b]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
cnt = 0

mat = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

dfs(0,0)
print(visited[0][0])

