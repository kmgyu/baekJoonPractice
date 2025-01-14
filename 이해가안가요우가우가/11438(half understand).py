LOG = 21
input = open(0).readline

# 11437에서 난이도가 올라감(제약조건) 코드는 같다.
# 개념은 이해했는데... 여기 어디에 희소배열이 씌였다는거?
# 왜 nlogn이 되는건데ㅔㅔㅔㅔㅔㅔㅔ

# depth calculation
def dfs():
    stack = [(1, 0)]
    while stack:
        cur, depth = stack.pop()
        c[cur] = True
        d[cur] = depth
        for y in graph[cur]:
            if c[y]: continue #visited
            parent[y][0] = cur
            stack.append((y, depth+1))


# A와 B의 최소 공통 조상을 찾는 함수
def lca(a, b):
    # A, B SWAP (b is bigger)
    if d[a] > d[b]:
        a, b = b, a
    # make depth same
    for i in range(LOG-1, -1, -1):
        if d[b] - d[a] >= (1 << i):
            b = parent[b][i]
    # parent check
    if a == b: return a
    for i in range(LOG-1, -1, -1):
        # parent finding from inverse
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

N = int(input())
parent = [[0] * LOG for _ in range(N + 1)] # 부모 노드 정보
d = [0] * (N + 1) # each node depth from root
c = [False] * (N + 1) # depth calculation check(visited)
graph = [[] for _ in range(N + 1)] # 트리를 인접리스트 형태로 표현

# graph mapping
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# parent mapping
dfs() # root Node : 1
for i in range(1, LOG):
    for j in range(1, N + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]
        
M = int(input())

for i in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))