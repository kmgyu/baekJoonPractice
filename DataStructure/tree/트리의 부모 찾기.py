from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
graph = dict()
for i in range(n-1):
    a, b = map(int, input().split())
    try:
        graph[a].append(b)
    except:
        graph[a] = [b]
    try:
        graph[b].append(a)
    except:
        graph[b] = [a]

ans = [0]*(n+1)
def bfs():
    q = deque([1])
    while q:
        search = q.popleft()
        for i in graph[search]:
            if ans[i] == 0 and i != 1:
                ans[i] = search
                q.append(i)

bfs()
for i in range(2, n+1):
    print(ans[i])