import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = 0
    while q:
        a, b = q.popleft()
        for i in range(4):
            cx = a + dx[i]
            cy = b + dy[i]
            
            if cx < 0 or cy < 0 or cx >= n or cy >= m: continue
            
            if visited[cx][cy] == -1:
                if board[cx][cy] == 0:
                    visited[cx][cy] = visited[a][b]
                    q.appendleft((cx,cy))
                else:
                    visited[cx][cy] = visited[a][b] + board[cx][cy]
                    q.append((cx,cy))

m, n = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[-1] * m for _ in range(n)]

bfs()

print(visited[n-1][m-1])