import sys
import math
from collections import defaultdict
sys.setrecursionlimit(10**6)

def input():
    return sys.stdin.readline().strip()

# 변수 초기화
n = 0
m = 0
adj = defaultdict(list)
parent = []
level = []
maxlevel = 0

def set_tree(node, pnode, lv):
    level[node] = lv
    parent[node][0] = pnode

    for i in range(1, maxlevel + 1):
        parent[node][i] = parent[parent[node][i - 1]][i - 1]

    for childnode in adj[node]:
        if childnode == pnode:
            continue
        set_tree(childnode, node, lv + 1)

def LCA(a, b):
    if a == 1 or b == 1:
        return 1

    # a, b 중 level이 더 높은 노드를 target으로 설정
    if level[a] < level[b]:
        a, b = b, a

    # 두 노드의 level을 같게 조정
    for i in range(maxlevel, -1, -1):
        if level[parent[a][i]] >= level[b]:
            a = parent[a][i]
    # 가장 높은 깊이에서 높이를 감소시키며 확인해야 한다.
    # 깊이 비교할 때 달라지는 부분을 찾아야 한다.
    # 아닌가? 잘 모르겠다.
    
    # 공통 조상 찾기
    if a == b:
        return a

    for i in range(maxlevel, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]

    return parent[a][0]

def init():
    global n, m, adj, parent, level, maxlevel

    n = int(input())

    adj = defaultdict(list)
    for _ in range(n - 1):
        p, c = map(int, input().split())
        adj[p].append(c)
        adj[c].append(p)

    maxlevel = int(math.floor(math.log2(100001)))
    parent = [[0] * (maxlevel + 1) for _ in range(n + 1)]
    level = [0] * (n + 1)

def main():
    init()

    set_tree(1, 0, 1)

    m = int(input())
    for _ in range(m):
        f, s = map(int, input().split())
        print(LCA(f, s))

if __name__ == "__main__":
    main()
