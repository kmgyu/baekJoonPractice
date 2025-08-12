# 왜 안돌아가는거임;
# import sys
# input = sys.stdin.readline

# n = int(input())

# for _ in range(n):
#     stream = input().split()
#     node = int(stream[0])
#     edge_l = int(stream[1])
    
#     edges = dict()
#     for i in range(1, edge_l+1):
#         a, b = stream[2*i], stream[2*i + 1]
#         a = int(a[1:])
#         b = int(b[1:])
        
#         if a not in edges: edges[a] = set()
#         if b not in edges: edges[b] = set()
#         edges[a].add(b)
#         edges[b].add(a)

#     supervillain = int(stream[-1][1:])
#     ans = 0
#     if supervillain in edges:
#         temp = edges[supervillain] # set
#         hop = set()
#         for i in temp:
#             hop |= edges[i]
#         hop |= temp
#         if supervillain in hop: hop.remove(supervillain)
#         ans = len(hop)
#     print(f"The number of supervillains in 2-hop neighborhood of v{supervillain} is {ans}")
    
from collections import deque

def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 0
    while q:
        node = q.popleft()
        for n in graph[node]:
            if check[n] == -1:
                q.append(n)
                check[n] = check[node]+1

for _ in range(int(input())):
    a = input().split()
    N, M = int(a[0]), int(a[1])
    vx = a[-1]
    graph = [[] for i in range(N+1)]
    li = a[2:-1]
    for i in range(M):
        u, v = int(li[i*2][1:]), int(li[i*2+1][1:])
        graph[u].append(v)
        graph[v].append(u)
    check = [-1]*(N+1)
    bfs(int(vx[1:]))
    res = sum([1 for t in check if 1 <= t <= 2])
    print(f"The number of supervillains in 2-hop neighborhood of {vx} is {res}")