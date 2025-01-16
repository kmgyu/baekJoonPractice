
# 재귀함수를 while문과 stack을 이용한 최적화
# 메모리 스택과 달라서 다시 짜야됨

# 초기화 이런식으로 하면 찐빠남.
def init(a, tree, n, s, e):
    stack = []
    stack.append((n, s, e))
    while stack:
        node, start, end = stack.pop()
        if start == end:
            tree[node] = a[start]
        else:
            stack.append((node*2, start, (start+end)//2))
            stack.append((node*2+1, (start+end)//2+1, end))
            tree[node] = tree[node*2] + tree[node*2+1]

# left, right : boundary
# 최적화했으나 시간은 더 늘어남.
def query(tree, node, start, end, left, right):
    stack = []
    stack.append((node, start, end))
    result = 0
    while stack:
        node, start, end = stack.pop()
        if left > end or right < start:
            continue
        if left <= start and end <= right:
            result += tree[node]
            continue
        stack.append((node*2, start, (start+end)//2))
        stack.append((node*2+1, (start+end)//2+1, end))
    return result

# 작동 안됨. stack append가 완료된 후 start==end 부분부터 update가 실행되어야 한다. append와 update가 동시에 실행되므로 수정필요.
def update(a, tree, node, start, end, index, val):
    stack = []
    stack.append((node, start, end))
    while stack:
        node, start, end = stack.pop()
        if index < start or index > end: continue
        if start == end:
            a[index] = val
            tree[node] = val
            continue
        stack.append((node*2, start, (start+end)//2))
        stack.append((node*2+1, (start+end)//2+1, end))
        tree[node] = tree[node*2] + tree[node*2+1]
