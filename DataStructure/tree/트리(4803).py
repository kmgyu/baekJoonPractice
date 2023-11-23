import sys
from collections import deque
input = sys.stdin.readline
c = 1
def findCycle(start):
    q = deque()
    q.append(start)
    isCycle = False
    
    while q:
        node = q.popleft()
        if visited[node]: isCycle=True
        for i in graph[node]:
            if visited[i] == 0:
                q.append(i)
        visited[node] = 1
    return isCycle

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0: break
    parent = list(range(n+1))
    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)


    cnt = 0
    for i in range(1, n+1):
        if visited[i]:
            continue
        if not findCycle(i):
            cnt += 1
    
    if cnt == 1:
        print(f"Case {c}: There is one tree.")
    elif cnt > 0:
        print(f"Case {c}: A forest of {cnt} trees.")
    else:
        print(f"Case {c}: No trees.")
    c += 1