from collections import deque

n = int(input()) #computer number
p = int(input()) #pair of computer
graph = dict()
visit = [False] * (n+1)
cnt = 0
for i in range(1, n+1):
    graph[i] = []

for i in range(p):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
while q:
    d = q.pop()
    if visit[d]: continue
    cnt += 1
    visit[d] = True
    for i in graph[d]:
        q.append(i)
print(cnt-1)