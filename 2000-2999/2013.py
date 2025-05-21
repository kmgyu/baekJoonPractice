# CCW
def ccw(a, b, c):
    ans = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    ans -= a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    if ans: return 1
    else: return 0 # 평행

# 무조건 기울기가 1이상인 벡터가 아닐 수 있다.
def p_comp(a, b):
    if a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]): a, b = b, a
    return a, b

# 선분 교차 판정 : 평행 케이스
def isIntersect(l1, l2):
    a, b = l1
    c, d = l2
    ab = ccw(a, b, c) == ccw(a, b, d) == 0
    cd = ccw(c, d, a) == ccw(c, d, b) == 0
    # '이어지는' 선 평행체크
    if ab and cd:
        a, b = p_comp(a, b)
        c, d = p_comp(c, d)
        # 거지 발싸개 같은 문제
        # 벡터 정렬
        return p_comp(c, b) == (c, b) and p_comp(a, d) == (a, d)
        # return c[0] <= b[0] and c[1] <= b[1] and a[0] <= d[0] and a[1] <= d[1]
    # 겹치는 경우 : b가 c보다 커서 c랑 b가 겹친다. d가 항상 a보다 커야 한다.
    # 안 그러면 그냥 평행함
    return 0

def find(n):
    if parent[n] != n: parent[n] = find(parent[n])
    return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a > b: a, b = b, a
    parent[b] = a

input = open(0).readline
N = int(input())
parent = list(range(N))
lines = []
for _ in range(N):
    # fucking floating point
    x1, y1, x2, y2 = map(lambda x: int(round(float(x)*100)), input().split()) 
    lines.append([(x1, y1), (x2, y2)])

for i in range(N-1):
    for j in range(i+1, N):
        if isIntersect(lines[i], lines[j]):
            # union
            union(i, j)

for i in range(N): parent[i] = find(i)

print(len(set(parent)))
