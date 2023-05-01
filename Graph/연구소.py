from itertools import combinations
from collections import deque
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
temp  = [[0] * m for _ in range(n)]
virus = []
empty = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i,j))
        if graph[i][j] == 0:
            empty.append((i,j))

candi_walls = combinations(empty,3)

def copy(grp,tmp):
    for i in range(n):
        for j in range(m):
            tmp[i][j] = grp[i][j]
    return tmp

def check_safe(tmp):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    return cnt

dx = [-1,  0 , 1, 0]
dy = [ 0 ,-1,  0, 1]
def bfs(grp,x,y):
    q = deque([(x,y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0<= nx < n and 0<= ny < m:
                if grp[nx][ny] != 0:
                    continue
                grp[nx][ny] = 2
                q.append((nx,ny))
    return grp

def print_gr(graph):
    for i in range(n):
        print(graph[i])


max_empty = 0
for can_wall in candi_walls:
    temp = copy(graph,temp)
    for x,y in can_wall:
        temp[x][y] = 1
    for x,y in virus:
        temp = bfs(temp,x,y)
    max_empty = max(check_safe(temp), max_empty)

print(max_empty)