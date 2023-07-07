# 0-1 BFS + 데이크스트라
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    
    while q:
        a, b = q.popleft()
        for i in range(4):
            cx = a + dx[i]
            cy = b + dy[i]
            
            if cx < 0 or cy < 0 or cx >= n or cy >= m: continue
            
            # 0 - 1 BFS
            if visited[cx][cy] == 0: # 첫 방문
                print("blah")
            
        
    


m, n = map(int, input().split()) #가로 m, 세로 n
maze = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0] * m for _ in range(n)] # 방문 및 거리

