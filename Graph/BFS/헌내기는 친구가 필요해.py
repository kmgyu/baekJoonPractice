import sys
from collections import deque
input = sys.stdin.readline

def solve(a, b):
    q = deque()
    q.append((a,b))
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            mx = x+dx[i]
            my = y+dy[i]
            if mx < 0 or mx >= n or my < 0 or my >= m: continue
            if visited[mx][my] or mat[mx][my] == 'X':continue
            if mat[mx][my] == 'P':
                cnt += 1
            q.append((mx, my))
            visited[mx][my] = True
    return cnt

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'I':
            ans = solve(i, j)
            if ans: print(ans)
            else: print("TT")
            exit()
