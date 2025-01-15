import math
input = open(0).readline

def init(a, tree, node, start, end):
    # segment tree 구성할 때 부터 원소에다 pair로 저장해줘야됨.
    if start == end:
        tree[node] = a[start], a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = min(tree[node*2][0], tree[node*2+1][0]), max(tree[node*2][1], tree[node*2+1][1])

def query(tree, node, start, end, left, right):
    # pair 쿼리
    if left > end or right < start: return float('inf'), 0
    if left <= start and end <= right: return tree[node]
    lmin, lmax = query(tree, node*2, start, (start+end)//2, left, right)
    rmin, rmax = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return min(lmin, rmin), max(lmax, rmax)

N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]
height = math.ceil(math.log2(N)) + 1
tree = [0] * (1 << height)

init(arr, tree, 1, 0, N-1)
for _ in range(M):
    a, b = map(int, input().split())
    print(*query(tree, 1, 0, N-1, a-1, b-1))