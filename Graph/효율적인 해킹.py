import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    visited = [False] * (n+1)
    q = deque()
    q.append(start)
    node[start]+=1
    visited[start] = True
    while q:
        x = q.popleft()
        for y in edge[x]:
            if visited[y]:continue
            visited[y] = True
            node[y] += 1
            q.append(y)


n, m = map(int, input().split())

edge = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)

node = [0]*(n+1)
big = 0
for i in range(1, n+1):
    bfs(i)

big = max(node)
for i in range(1, n+1):
    if big == node[i]:
        print(i, end = ' ')
