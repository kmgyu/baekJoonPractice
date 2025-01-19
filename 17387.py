def ccw(a, b, c):
    ans = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    ans -= a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    if ans > 0: return 1 # 반시계
    elif ans < 0: return -1 # 시계
    else: return 0 # 평행

def isIntersect(l1, l2):
    a, b = l1
    c, d = l2
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab == 0 and cd == 0:
        if a > b: a,b=b,a
        if c > d: c,d=d,c
        return c <= b and a <= d
    return ab <= 0 and cd <= 0

L1 = [*map(int, input().split())]
L2 = [*map(int, input().split())]

L1 = [L1[:2], L1[2:]]
L2 = [L2[:2], L2[2:]]
print(isIntersect(L1, L2)&1)