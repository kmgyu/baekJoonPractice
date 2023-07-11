import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
# https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-1967-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%8A%B8%EB%A6%AC%EC%9D%98-%EC%A7%80%EB%A6%84-%EA%B3%A8%EB%93%9C-4-%ED%8A%B8%EB%A6%AC

def dfs(node, edge):
    for n, w in tree[node]:
        cur_edge = edge + w
        if visited[n] == -1:
            visited[n] = cur_edge
            dfs(n, cur_edge)
    return

n = int(input())
tree = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
visited[1] = 0

for i in range(n-1):
    a, b, c = map(int, input().split())
    # 부모 자식 간선
    tree[a].append((b,c))
    tree[b].append((a,c))

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