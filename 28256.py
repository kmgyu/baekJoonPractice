import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    if visited[x][y] or choco[x][y] != 'O':
        return
    ans = 0
    while q:
        lx, ly = q.popleft()
        if visited[lx][ly]:continue
        visited[lx][ly] = True
        ans += 1
        for i in range(4):
            cx = lx + dx[i]
            cy = ly + dy[i]
            if cx < 0 or cx > 2 or cy < 0 or cy > 2: continue
            if visited[cx][cy] or choco[cx][cy] == '-': continue
            if choco[cx][cy] == 'O':
                q.append((cx, cy))
    result.append(ans)


t = int(input())
for i in range(t):
    choco = [list(map(str, input().rstrip())) for _ in range(3)]
    visited = [[False] * 3 for _ in range(3)]
    mid = list(map(int, input().split()))
    result = []
    for i in range(3):
        for j in range(3):
            bfs(i,j)
    if mid[1:] == sorted(result): print(1)
    else: print(0)