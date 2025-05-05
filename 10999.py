# lazy update segment tree


def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def query(tree, lazy, node, start, end, left, right):
    lazy_update(tree, lazy, node, start, end)
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, lazy, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, lazy, node*2+1, (start+end)//2+1, end, left, right)
    return lsum + rsum

def lazy_update(tree, lazy, node, start, end):
    if lazy[node] != 0:
        tree[node] += (end-start+1)*lazy[node]
        if start != end:
            lazy[node*2] += lazy[node]
            lazy[node*2+1] += lazy[node]
        lazy[node] = 0

def update_range(tree, lazy, node, start, end, left, right, diff):
    lazy_update(tree, lazy, node, start, end)
    if left > end or right < start:
        return
    if left <= start and end <= right:
        tree[node] += (end-start+1) * diff
        if start != end:
            lazy[node*2] += diff
            lazy[node*2+1] += diff
        return
    update_range(tree, lazy, node*2, start, (start+end)//2, left, right, diff)
    update_range(tree, lazy, node*2+1, (start+end)//2+1, end, left, right, diff)
    tree[node] = tree[node*2] + tree[node*2+1]

input = open(0).readline

N, M, K = map(int, input().split())

import math
height = math.ceil(math.log2(N)) + 1

# tree init
arr = [int(input()) for _ in range(N)]
tree = [0] * (2**height)
lazy = [0] * (2**height)

init(arr, tree, 1, 0, N-1)
# print(tree)
for _ in range(M + K):
    quest = [*map(int, input().split())]
    if quest[0] == 1:
        a,b,c,d = quest
        update_range(tree, lazy, 1, 0, N-1, b-1, c-1, d)
    else:
        a,b,c = quest
        print(query(tree, lazy, 1, 0, N-1, b-1, c-1))
