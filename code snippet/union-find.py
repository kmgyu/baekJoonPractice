# 분리 집합을 빠르게 찾고 합치는 알고리즘

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

# find and union
# 더 더 더 함축시켰다. 대신 parent < chldren이 보장되는지는 몰루. 기억안나 ㅎ
def find(n):
    if parent[n] == n:
        return n
    parent[n] = find(parent[n])
    return parent[n]

# test driver
N = 10
parent = [i for i in range(N+1)] # parent는 self입니다. lol