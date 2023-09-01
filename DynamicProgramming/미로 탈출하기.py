import sys
sys.setrecursionlimit(10**6)
def input(): return sys.stdin.readline().rstrip()

def solve(x, y):
    if visited[x][y]: return escape[x][y]
    
    idx = com.index(maze[x][y])
    visited[x][y] = True
    mx = x+dx[idx]
    my = y+dy[idx]
    if mx < 0 or mx >= n or my < 0 or my >= m:
        escape[x][y] = True
    elif solve(mx, my):
        escape[x][y] = True
    
    return escape[x][y]

com = ['U', 'D', 'R', 'L'] #comparison
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
escape = [[False]*m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if solve(i, j):
            cnt += 1

print(cnt)