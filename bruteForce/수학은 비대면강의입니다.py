a, b, c, d, e, f = map(int, input().split())
x = 0
if b != 0:
    m = d*b - a*e
    n = f*b - c*e
    for i in range(-999, 1000):
        if (m * i) == n:
            x = i

    y = int((c - a*x)/b)

else:
    x = int(c/a)
    y = int((f-d*c/a)/e)

print(f'{x} {y}')