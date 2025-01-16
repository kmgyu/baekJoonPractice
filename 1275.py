import math
def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
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

N, Q = map(int, input().split())

arr = list(map(int, input().split()))
height = math.ceil(math.log2(N)) + 1
tree = [0] * (1 << height)

init(arr, tree, 1, 0, N-1)

for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x>y: x, y = y, x
    print(query(tree, 1, 0, N-1, x-1, y-1))
    update(arr, tree, 1, 0, N-1, a-1, b)