# https://www.acmicpc.net/source/44833278
# union-find
# 왜 내껀 자꾸 틀리는데 개빡치게

# def find(n):
#     if parent[n] == n: return n
#     parent[n] = find(parent[n])
#     return parent[n]

# N = int(input())

# if N == 1:
#     print(0)
#     exit()

# mat = []
# parent = [-1 for _ in range(N)]

# for i in range(N):
#     line = input()
#     for j in range(i+1, N):
#         if line[j] == 'Y':
#             parent[i] = i
#             parent[j] = j
#             mat.append((i, j))

# for i, j in mat: parent[j] = find(parent[i])

# parent_ = set(parent)

# if len(mat) < (N-1) or -1 in parent_: print(-1)
# else: print(len(parent_)-1)

# 연결 조건 : 일단 노드들을 전부 연결할 수 있어야 하는데 최소 엣지가 N-1개 필요함.
# 왜 자꾸 처 틀리는데
import sys
input = sys.stdin.readline

N = int(input())
maps = [input().strip() for _ in range(N)]

if N == 1 :
  print(0)
  exit()

visited = [False]*N
edge_list = list()

def dfs(node) :
  q = [ node ]
  visited[node] = True
  edges, nodes = 0, 0

  while q :
    node = q.pop()
    nodes += 1
    for i in range(N) :
      if maps[node][i] == 'N' :
        continue
      edges += 1
      if not visited[i] :
        visited[i] = True
        q.append(i)
  edge_list.append((nodes, edges // 2))

for i in range(N) :
  if not visited[i] :
    dfs(i)

enable = True
cnt = 0
for nodes, edges in edge_list :
  if nodes == 1 :
    enable = False
    break
  cnt += edges - nodes + 1

print(len(edge_list) - 1 if enable and cnt >= len(edge_list)-1 else -1)

