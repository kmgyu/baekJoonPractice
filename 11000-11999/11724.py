from collections import deque
from sys import stdin
input = stdin.readline

n, m = map(int, input().split()) #node = m, connect = n
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(pos):
    visited[pos] = True
    queue = deque([pos])
    while queue:
        for i in graph[queue.popleft()]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)


cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        cnt+=1
print(cnt)