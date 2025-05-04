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
        a[index] += val
        tree[node] += val
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]

input = open(0).readline

N, M, K = map(int, input().split())

import math
height = math.ceil(math.log2(N)) + 1

# tree init
arr = [int(input()) for _ in range(N)]
tree = [0] * (2**height)

init(arr, tree, 1, 0, N-1)
# print(tree)
for _ in range(M + K):
    quest = [*map(int, input().split())]
    if quest[0] == 1:
        a,b,c,d = quest
        for idx in range(b-1, c):
            arr[idx] += d
        init(arr, tree, 1, 0, N-1) # lazy init
        # 브랜치를 갱신하는 법만 강구해야 할듯
        # print(arr)
        # print(tree)
    else:
        a,b,c = quest
        print(query(tree, 1, 0, N-1, b-1, c))
