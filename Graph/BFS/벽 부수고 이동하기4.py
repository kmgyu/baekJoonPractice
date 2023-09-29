from collections import deque
import sys
def input() : return sys.stdin.readline().rstrip()

zeroSet = 0
zeroCnt = []

def bfs_search(a, b):
    global zeroSet
    if mat[a][b]: return
    q = deque()
    q.append((a, b))
    visited[a][b] = zeroSet
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            mx = x+dx[i]
            my = y+dy[i]
            if mx < 0 or my < 0 or mx >= n or my >= m: continue
            if visited[mx][my] >= 0 or mat[mx][my]: continue
            visited[mx][my] = zeroSet
            q.append((mx, my))
            cnt += 1
    zeroCnt.append(cnt)
    zeroSet += 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


n, m = map(int, input().split())
mat = [list(map(int, input())) for _ in range(n)]
ans_mat = [[0]*m for _ in range(n)]
visited = [[-1]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if visited[i][j] == -1:
            bfs_search(i, j)

for i in range(n):
    for j in range(m):
        if mat[i][j]:
            zero_avail = set()
            for k in range(4):
                if 0<=i+dx[k]<n and 0<=j+dy[k]<m:
                    zero_avail.add(visited[i+dx[k]][j+dy[k]])
            cnt = 1
            for z in zero_avail:
                if z == -1: continue
                cnt += zeroCnt[z]
            ans_mat[i][j] = cnt%10

for line in ans_mat:
    print(*line, sep="")