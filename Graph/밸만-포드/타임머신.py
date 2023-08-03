import sys
from math import inf
input = sys.stdin.readline

n, m = map(int, input().split())
dist = [inf] * (n+1)
edges = []

for i in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

dist[1] = 0
for i in range(1, n+1):
    for edge in edges:
        if dist[edge[0]] != inf and dist[edge[1]] > dist[edge[0]] + edge[2]:
            dist[edge[1]] = dist[edge[0]] + edge[2]
            if i == n:
                print(-1)
                exit()

for i in range(2, n+1):
    print(dist[i]) if dist[i] != inf else print(-1)