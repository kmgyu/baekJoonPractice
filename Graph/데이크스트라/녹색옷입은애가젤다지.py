from sys import stdin
from collections import deque
input = stdin.readline
#다익스트라 알고리즘

t = 1
while True:
    n = int(input())
    if n == 0: break
    path = []
    visited = [[False]*n for _ in range(n)]
    for _ in range(n):
        path.append(list(map(int, input().rstrip().split())))

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    map_ = [[10e9]*n for _ in range(n)]
    map_[0][0] = path[0][0]
    q = deque()
    visited[0][0] = True
    visited[1][0] = True
    visited[0][1] = True
    q.append([0,1])
    q.append([1,0])
    while q:
        x, y = q.popleft()
        for i in range(4):
            mx = x+dx[i]
            my = y+dy[i]
            if mx < 0 or my < 0 or mx >= n or my >= n: continue
            if not visited[mx][my]:
                visited[mx][my] = True
                q.append([mx,my])
            if map_[mx][my]+path[x][y] < map_[x][y]: # 현재 위치 최단거리 갱신
                map_[x][y] = map_[mx][my]+path[x][y]
                q.append([mx,my])
            if map_[x][y]+path[mx][my] < map_[mx][my]: # 조사 위치 최단거리 갱신
                map_[mx][my] = map_[x][y]+path[mx][my]
                q.append([mx,my])
    
    print(f"Problem {t}: {map_[n-1][n-1]}")
    t+=1