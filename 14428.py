import math
input = open(0).readline

def init(a, tree, node, start, end):
    if start == end:
        tree[node] = start
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] if arr[tree[node*2]] <= arr[tree[node*2+1]] else tree[node*2+1]

def query(tree, node, start, end, left, right):
    global arr
    stack = []
    stack.append((node, start, end))
    result = -1 # index of arr
    while stack:
        node, start, end = stack.pop()
        if left > end or right < start:
            continue
        if left <= start and end <= right:
            # print(arr[result], arr[tree[node]], tree[node], result)
            result = tree[node] if result < 0 or arr[result] > arr[tree[node]] else result
            if arr[result] == arr[tree[node]]: result = min(result, tree[node])
            continue
        stack.append((node*2, start, (start+end)//2))
        stack.append((node*2+1, (start+end)//2+1, end))
    return result

def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = index
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2] if arr[tree[node*2]] <= arr[tree[node*2+1]] else tree[node*2+1]

N = int(input())
arr = [*map(int, input().split())]
M = int(input())

height = math.ceil(math.log2(N)) + 1
tree = [0] * (1 << height)
init(arr, tree, 1, 0, N-1)

for _ in range(M):
    q, i, j = map(int, input().split())
    if q==1: update(arr, tree, 1, 0, N-1, i-1, j)
    else: print(query(tree, 1, 0, N-1, i-1, j-1)+1)