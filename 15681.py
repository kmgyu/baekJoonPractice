import sys
sys.setrecursionlimit(10**6)

# 트리의 dp란 이런 것이다..?

input = open(0).readline
N, R, Q = map(int, input().split())
graph = dict()
for i in range(N-1):
    a, b = map(int, input().split())
    if a not in graph: graph[a] = []
    if b not in graph: graph[b] = []
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
def dfs(node):
    visited[node] = 1
    for i in graph[node]:
        if visited[i]: continue
        visited[node] += dfs(i)
    return visited[node]

dfs(R)
for _ in range(Q): print(visited[(int(input()))])