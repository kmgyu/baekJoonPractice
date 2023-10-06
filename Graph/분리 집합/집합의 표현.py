import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 찾기 연산(같은 집합에 속하는지 확인하기 위한 함수)
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

# 합집합 연산(두 집합을 합치기 위한 함수)
def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: # 값이 더 작은 쪽을 부모로
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n+1)]
for i in range(m):
    k, a, b = map(int, input().split())
    
    if k:
        if find_parent(a) == find_parent(b):print("yes")
        else:print("no")
    else:
        union_parent(a, b)
