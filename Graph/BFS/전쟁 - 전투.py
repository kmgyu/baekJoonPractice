from collections import deque
import sys

input = sys.stdin.readline

def bfs(x, y, color):
    cnt = 1
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for mx, my in zip(dx, dy):
            nx, ny = x+mx, y+my
            if 0 <= nx < n and 0 <= ny < m and mat[nx][ny] == color and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

m, n = map(int, input().split())
mat = [input() for _ in range(n)]
visited = [[False]*m for _ in range(n)]
answer = [0, 0]


for i in range(n):
    for j in range(m):
        if visited[i][j]: continue
        cnt = bfs(i, j, mat[i][j])**2
        answer[0] += cnt if mat[i][j] == 'W' else 0
        answer[1] += cnt if mat[i][j] == 'B' else 0
print(*answer)