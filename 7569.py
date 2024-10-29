import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs():
    q = deque()
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if boxes[i][j][k] == 1:
                    q.append((i, j, k))
    
    while q:
        x, y, z = q.popleft()
        
        for i in range(6):
            cx = x + dx[i]
            cy = y + dy[i]
            cz = z + dz[i]
            if cx < 0 or cx >= h or cy < 0 or cy >= n or cz < 0 or cz >= m: continue
            if boxes[cx][cy][cz] == 0:
                q.append((cx, cy, cz))
                boxes[cx][cy][cz] = boxes[x][y][z] + 1
    ans = 0
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if boxes[i][j][k] == 0: return -1
                ans = max(ans, boxes[i][j][k])
    return ans-1


boxes = []

m, n, h = map(int, input().split())

for i in range(h):
    box = [list(map(int, input().split())) for _ in range(n)]
    boxes.append(box)

print(bfs())