def ccw(a, b, c):
    ans = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    ans -= a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    if ans > 0: return 1
    elif ans < 0: return -1 
    else: return 0 

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

input = open(0).readline

N = int(input())

parent = list(range(N))

edges = []
for _ in range(N):
    x1, y1, x2, y2, w = map(int, input().split())
    edges.append(((x1, y1), (x2, y2), w))

edges.sort(key=lambda x: x[-1])

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        if isIntersect(edges[i][:-1], edges[j][:-1]):
            ans += edges[i][-1]

print(ans+sum(map(lambda x: x[-1], edges)))