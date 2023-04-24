from collections import deque
from sys import stdin
input = stdin.readline

def bfs(pos, visited):
    visited[pos] = 1
    que = deque([pos])
    while que:
        current = que.popleft()
        for i in graph[current]:
            if visited[i] == 0:
                visited[i] = visited[current] * -1
                que.append(i)
            elif visited[i] == visited[current]:
                return False
    return True

t = int(input()) #test case
for i in range(t):
    v, e = map(int, input().split()) #node = v, relation = e
    graph = [[] for _ in range(v+1)]
    visited = [0] * (v+1) # divide 1 or -1
    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    isT = True
    for i in range(1, v+1):
        if visited[i] != 0:
            continue
        if not bfs(i, visited):
            isT = False
            break
    if isT:
        print("YES")
    else:
        print("NO")
