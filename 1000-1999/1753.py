import sys
from heapq import heappush, heappop
from math import inf
input = sys.stdin.readline

def bfs(x):
    q = []
    heappush(q, (0, x))
    dist[x] = 0
    while q:
        d, node = heappop(q)
        for e, c in graph[node]:
            if dist[e] > d + c:
                dist[e] = d + c
                heappush(q, (d + c, e))
    return dist


v, e = map(int, input().split()) # vertex / edge
k = int(input()) # 시작 정점 번호
graph = [[] for _ in range(v+1)]
dist = [inf] * (v+1)

for _ in range(e):
    u, v, w = map(int, input().split()) # u to v cost w
    graph[u].append((v, w))

bfs(k)

for i in dist[1:]:
    if i == inf:print("INF")
    else:print(i)
