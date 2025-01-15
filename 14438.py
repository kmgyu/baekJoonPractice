import math
input = open(0).readline

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = min(tree[node*2], tree[node*2+1])

def query(tree, node, start, end, left, right):
    if left > end or right < start: return float('inf')
    if left <= start and end <= right: return tree[node]
    lmin = query(tree, node*2, start, (start+end)//2, left, right)
    rmin = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return min(lmin, rmin)

def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = min(tree[node*2], tree[node*2+1])

N = int(input())
arr = [*map(int, input().split())]
M = int(input())

height = math.ceil(math.log2(N)) + 1
tree = [0] * (1 << height)
init(arr, tree, 1, 0, N-1)

for _ in range(M):
    q, i, j = map(int, input().split())
    if q==1: update(arr, tree, 1, 0, N-1, i-1, j)
    else: print(query(tree, 1, 0, N-1, i-1, j-1))
