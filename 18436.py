import math
def init(a, tree, node, start, end):
    if start == end:
        tree[node][(a[start]&1)] = 1
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
        tree[node][1] = tree[node*2][1] + tree[node*2+1][1]

def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return (0, 0)
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum[0] + rsum[0], lsum[1] + rsum[1]

def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node][val&1] = 1
        tree[node][not val&1] = 0
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
    tree[node][1] = tree[node*2][1] + tree[node*2+1][1]
    
input = open(0).readline

N = int(input())

arr = [*map(int, input().split())]
height = math.ceil(math.log2(N)) + 1
tree = [[0, 0] for _ in range(1<<height)]

init(arr, tree, 1, 0, N-1)

M=int(input())

for _ in range(M):
    i, l, r = map(int, input().split())
    if i == 1:
        update(arr, tree, 1, 0, N-1, l-1, r)
    elif l>r: l, r = r, l
    if i == 2:
        print(query(tree, 1, 0, N-1, l-1, r-1)[0])
    elif i == 3:
        print(query(tree, 1, 0, N-1, l-1, r-1)[1])