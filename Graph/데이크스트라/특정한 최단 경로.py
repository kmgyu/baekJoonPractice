from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def bfs(n1):
    global v1, v2, n
    visited = [-1]*(n+1)
    heap = []
    heap.append(n1)
    visited[n1] = 0
    while heap:
        node = heappop(heap)
        for v, e in graph[node]:
            if visited[v] == -1 or visited[v] > visited[node]+e:
                visited[v] = visited[node]+e
                heappush(heap, v)
    return visited[v1], visited[v2], visited[n]

n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]


for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split()) # 반드시 지나야함

start = bfs(1)
v1s = bfs(v1)
v2s = bfs(v2)
if -1 in start: print(-1)
else: print(min(start[0] + v1s[1] + v2s[2], start[1]+ v2s[0] + v1s[2]))
# min(bfs(1, v1) + bfs(v1, v2) + bfs(v2, n), bfs(1, v2) + bfs(v2, v1) + bfs(v1, n))