import sys
import math
sys.setrecursionlimit(10**6)

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def query(tree, node, start, end, left, right):
    if left > end or right < start: return 0
    if left <= start and end <= right: return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum

def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]

input = open(0).readline

N, M, K = map(int, input().split())

arr = [int(input()) for _ in range(N)]
height = math.ceil(math.log2(N)) + 1
tree = [0] * (1 << height) # much faster than power. maybe it's technics?

init(arr, tree, 1, 0, N-1)

for i in range(M+K):
    a, b, c = map(int, input().split())
    if a == 1: update(arr, tree, 1, 0, N-1, b-1, c)
    else: print(query(tree, 1, 0, N-1, b-1, c-1))