import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def bfs(x, distance):
    q = []
    heappush(q, (0, x))
    distance[x] = 0
    while q:
        dis, cNode = heappop(q)
        for end, cost in graph[cNode]:
            if distance[end] == -1:
                distance[end] = dis + cost
                heappush(q, (dis + cost, end))
            elif distance[end] > dis + cost:
                distance[end] = dis + cost
                heappush(q, (dis + cost, end))

    return distance

n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1) # + visited

for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((end, cost))

distance = bfs(x, distance)


for i in range(1, n+1):
    tmp = [-1] * (n+1)
    if i == x: continue
    tmp = bfs(i, tmp)
    distance[i] += tmp[x]

print(max(distance))