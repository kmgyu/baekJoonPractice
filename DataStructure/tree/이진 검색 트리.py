import sys

def postorder(start, end):
    if start >= end:
        return
    if start == end - 1:
        print(tree[start])
        return
    idx = start + 1 #오른쪽 자식 노드 찾기
    while idx < end: # 부모보다 커질때까지 더해주면 됨.
        if tree[start] < tree[idx]:
            break
        idx += 1
    postorder(start+1, idx) #왼쪽 재귀
    postorder(idx, end) #오른쪽 재귀
    print(tree[start])

sys.setrecursionlimit(20000)
input = sys.stdin.readline
tree = []

while True:
    try:
        tree.append(int(input()))
    except:
        break
postorder(0, len(tree))