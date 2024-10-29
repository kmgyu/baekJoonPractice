import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(node, edge):
    for n, w in tree[node]:
        cur_edge = edge + w
        if visited[n] == -1:
            visited[n] = cur_edge
            dfs(n, cur_edge)
    return


n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n):
    s = list(map(int, input().split()))
    for i in range(1, len(s), 2):
        if s[i] == -1: break
        tree[s[0]].append((s[i], s[i+1]))

visited = [-1]*(n+1)
visited[1] = 0

dfs(1, 0)
idx, edge = 0, 0
for i in range(1, n+1):
    if visited[i] > edge:
        edge = visited[i]
        idx = i

visited = [-1]*(n+1)
visited[idx] = 0
dfs(idx, 0)

print(max(visited))