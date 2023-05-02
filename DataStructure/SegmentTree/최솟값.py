# a: 배열 A
# tree: 세그먼트 트리
# node: 노드 번호
# node에 저장되어 있는 합의 범위가 start - end
def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]
n, m = map(int, input().split())
tree=[0]*(n*2)
a = []
for i in range(n):
    a.append(int(input()))
init(a, tree, 0, 0, n-1)
print(tree)
print(sum(a[:5]))