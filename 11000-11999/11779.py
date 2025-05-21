import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = float('inf')

def bfs(start, end):
    q = [(0, start)]
    dist[start] = 0
    while q:
        cost, node = heappop(q)
        if cost > dist[node]: continue
        for c, e in graph[node]:
            if dist[e] > cost + c:
                dist[e] = cost + c
                parents[e] = node
                if e != end:
                    heappush(q, (cost + c, e))
    return dist[end]

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
dist = [inf] * (n+1)
parents = list(range(n+1))

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
start, end = map(int, input().split())


print(bfs(start, end))

tmp = end
answer = [tmp]
while tmp != start:
    tmp = parents[tmp]
    answer.append(tmp)
    

print(len(answer))
print(*answer[::-1])