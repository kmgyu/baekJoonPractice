# 요구사항 1 - 그림의 넓이 구하기 (최댓값)
# 요구사항 2 - 그림의 갯수 구하기
# 조건 1 - 주변 4칸으로 연결되어야 하나의 그림.
# 조건 2 - 가로, 세로 각각 500 이하
# 조건 3 - 그림은 없을 수 있다.

import sys
from collections import deque

input = sys.stdin.readline

mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    
    size = 0
    
    while q:
        cx, cy = q.popleft()
        size += 1
        for i in range(4):
            nx, ny = cx + mx[i], cy + my[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] :
                if pic[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
    return size

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * m for _ in range(n)]

paint = []

for i in range(n):
    for j in range(m):
        if visited[i][j] or not pic[i][j]: continue
        paint.append(bfs(i, j))

# 그림이 존재하지 않을 경우, 0 출력.
# 조건 빼먹지 말 것...
if paint:
    print(len(paint))
    print(max(paint))
else:
    print(0)
    print(0)