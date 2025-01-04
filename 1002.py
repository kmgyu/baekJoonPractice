t = int(input())
for i in range(0, t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r3 = ((x1-x2) ** 2 + (y1-y2) ** 2)
    a = (r1+r2) ** 2
    b = abs(r1-r2) ** 2
    if r3 == 0 and r1 == r2:
        print(-1)
    elif a == r3:
        print(1)
    elif b == r3:
        print(1)
    elif b > r3:
        print(0)
    elif a < r3:
        print(0)
    elif b < r3 < a:
        print(2)