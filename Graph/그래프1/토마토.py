# https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8

from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

graph = [[-1]*(n+2) for _ in range(m+2)]
que = deque()

for i in range(1, m+1):
    li = list(map(int, input().split()))
    for j in range(1, n+1):
        graph[i][j] = li[j-1]
        if li[j-1] == 1:
            que.append([i,j])


while que:
    x, y = que.popleft()
    for i in range(4):
        next_x = x+dx[i]
        next_y = y+dy[i]
        if graph[next_x][next_y] == 0:
            graph[next_x][next_y] = graph[x][y]+1
            que.append([next_x,next_y])
ans = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(i))
print(ans-1)
