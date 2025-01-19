# 선분 교차 판별을 이용해 풀 수 있는 문제
# 선분 교차 판별 시 <=를 이용해 교차 여부를 판별했는데
# 여러 케이스 중 평행한 선분이 있었다.
# 해당 케이스인 ==를 이용해 평행한 선분을 판별하면 된다.

# CCW
def ccw(a, b, c):
    ans = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    ans -= a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    if ans > 0: return 1 # 반시계
    elif ans < 0: return -1 # 시계
    else: return 0 # 평행

# 선분 교차 판정 : 평행 케이스
def isIntersect(l1, l2):
    a, b = l1
    c, d = l2
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab == 0 and cd == 0:
        if a > b: a,b=b,a
        if c > d: c,d=d,c
        return c == b and a == d
    return ab == 0 and cd == 0

input = open(0).readline
N = int(input())
numbering = [-1]*N
lines = []
for _ in range(N):
    x1, y1, x2, y2 = map(float, input().split())
    lines.append([(x1, y1), (x2, y2)])
