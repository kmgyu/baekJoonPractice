from heapq import heappush, heappop
# from math import inf
import sys
input = sys.stdin.readline
inf = int(1e9)
# 최단 경로가 여러 개 있을수도 있기 때문에 해당 문제에서는 1e9로 선언이 적합함. math.inf쓰면 틀린다.
# math.inf + 어떤 양수 = inf가 되기 때문...
def bfs(n1):
    global n, inf
    visited = [inf]*(n+1)
    heap = []
    heap.append((0, n1))
    visited[n1] = 0
    while heap:
        c, node = heappop(heap)
        if c > visited[node]: continue
        for v, e in graph[node]:
            if visited[v] > c+e:
                visited[v] = c+e
                heappush(heap, (visited[v], v))
    return visited

for _ in range(int(input())):
    # 교차로 = node
    n, m, t = map(int, input().split()) # 교차로, 도로, 목적지 후보
    s, g, h = map(int, input().split()) # 출발지, g와 h 교차로를 지나감

    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b, d = map(int, input().split()) # 양방향 그래프, 가중치
        graph[a].append((b,d))
        graph[b].append((a,d))

    cost = 0 #지나는 그래프가중치 찾기
    for v, e in graph[g]:
        if v == h:
            cost = e
            break


    endNode = [int(input()) for _ in range(t)] #도착지 후보
    endNode.sort()

    start = bfs(s) #g로 향하는 최단거리 + cost + middle == start에서의 최단거리여야함
    # cost += min(start[g], start[h])
    middle1 = bfs(h)
    middle2 = bfs(g)

    ans = []
    for node in endNode:
        if (cost + start[g] + middle1[node]) == start[node] or (cost + start[h] + middle2[node]) == start[node]:
            ans.append(node)
        # print(node, cost+middle1[node], start[node], cost + middle2[node])
    print(*ans)