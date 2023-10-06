import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

inf = int(1e9)

def bfs(start):
    visit = [inf] * (n+1)
    heap = [(-inf, start)]
    visit[start] = 0
    while heap:
        cost, node = heappop(heap)
        if node == end: print(-cost); return
        for next_node, w in graph[node]:
            if visit[next_node] > w:
                visit[next_node] = w
                heappush(heap, (max(cost, w), next_node))
    print(-visit[end])

n, m = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, -c))
    graph[b].append((a, -c))

start, end = map(int, input().split())
bfs(start)
