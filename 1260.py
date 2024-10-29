import sys
from collections import deque
input = sys.stdin.readline

def DFS(v):
    visited[v]=1
    dfs.append(v)
    for i in node[v]:
        if not visited[i]:
            DFS(i)

def BFS(v):
    visited[v]=1
    bfs.append(v)
    q = deque()
    q.append(v)

    while q:
        for i in node[q.popleft()]:
            if(visited[i]==0):
                visited[i]=1
                bfs.append(i)
                q.append(i)

N, M, V = map(int, input().split())

node = dict()
for i in range(N+1):
    node[i] = list()
visited = [0]*(N+1)
dfs = []
bfs = []

for i in range(M):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

for j in range(N+1): node[j].sort()

DFS(V)
visited = [0]*(N+1)
BFS(V)

print(*dfs, sep=' ')
print(*bfs, sep=' ')