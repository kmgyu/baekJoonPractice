from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
man = list(range(n))
graph = [[] for _ in range(n)]
visited = [False] * n
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
isT = False
def dfs(pos, cnt): #시작 노드, 친구
    global isT
    visited[pos] = True
    if cnt == 4:
        isT = True
        return
    for i in graph[pos]:
        if not visited[i]:
            visited[i] = True
            dfs(i, cnt + 1)
            visited[i] = False
            
for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if isT:
        break
if isT:
    print(1)
else:
    print(0)