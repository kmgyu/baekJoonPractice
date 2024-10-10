import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    q = deque()
    visited = [0] * (n+1)
    visited[start] = 1
    q.append((start, 0))
    
    while q:
        x, e = q.popleft()
        if x == end : return e
        for i,w in graph[x]:
            if not visited[i]:
                visited[i] = 1
                q.append((i, w+e))

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

for _ in range(m):
    a, b = map(int, input().split())
    print(bfs(a, b))