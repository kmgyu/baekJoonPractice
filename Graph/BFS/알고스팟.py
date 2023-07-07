import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((1,1))
    
    while q:
        a, b = q.popleft()
        for i in range(4):
            cx = a + dx[i]
            cy = b + dy[i]
            
            if cx < 0 or cy < 0 or cx >= n or cy >= m: continue
            if cx == cy == 0 : continue
            
            
            if visited[cx][cy] == 0:
                if board[cx][cy] == 0:
                    visited[cx][cy] = visited[a][b]
                    if cx == n-1 and cy == m-1: continue
                    q.appendleft((cx, cy))
                    
                else:
                    q.append((cx,cy))
                    visited[cx][cy] = visited[a][b]+1
                    
            elif visited[cx][cy] > visited[a][b] and board[cx][cy] == 0:
                visited[cx][cy] = visited[a][b]
                if cx == n-1 and cy == m-1: continue
                q.appendleft((cx,cy))
                
            elif visited[cx][cy] > visited[a][b]-1:
                q.append((cx,cy))
                visited[cx][cy] = visited[a][b]+1
    



n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

bfs()
print(*visited, sep="\n")
print(visited[n-1][m-1])