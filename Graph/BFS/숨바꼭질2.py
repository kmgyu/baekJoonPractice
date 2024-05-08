import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
max_num = 100000
graph = [0] * (max_num + 1)
result = float('inf')
cnt = 0
def bfs(v):
    global result, cnt
    q = deque()
    q.append(v)

    while q:
        v = q.popleft()
        if v == k:
            result = min(result, graph[v])
            cnt += 1
            continue
        for nx in (v-1, v+1, 2*v):
            if nx < 0 or nx > max_num: continue
            if graph[nx] == 0 or graph[nx] == graph[v]+1:
                graph[nx] = graph[v] + 1
                q.append(nx)
bfs(n)

print(result)
print(cnt)

