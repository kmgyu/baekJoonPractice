def ccw(a, b, c):
    ans = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    ans -= a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    if ans > 0: return 1
    elif ans < 0: return -1
    else: return 0

# 4등분 해야해서 끝에 겹칠 경우는 0을 출력해야 한다. 끄으윽...
# 그래서 등호 빼줬당.
def isIntersect(l1, l2):
    a, b = l1
    c, d = l2
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    ans = 0
    if ab == 0 and cd == 0:
        if a > b: a,b=b,a
        if c > d: c,d=d,c
        ans = c < b and a < d
    ans = ab < 0 and cd < 0
    return ans&1

x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())

L1 = [(x1, y1), (x2, y2)]
L2 = [(x3, y3), (x4, y4)]
print(isIntersect(L1, L2))