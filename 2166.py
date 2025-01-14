import sys
input = sys.stdin.readline

def ccw(a, b, c):
    return ((a[0]*b[1] + b[0]*c[1] + c[0]*a[1]) - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])) / 2
    # x1*y2 + x2*y3 + x3*y1 - (y1*x2 + y2*x3 + y3*x1)

n = int(input())
coor = []
for i in range(n):
    x, y = map(int, input().split())
    coor.append((x, y))

ans = .0
for i in range(1, n-1):
    ans += ccw(coor[0], coor[i], coor[i+1])
print(f"{abs(ans):.1f}")