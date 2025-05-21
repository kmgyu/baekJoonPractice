from sys import stdin
input = stdin.readline
for _ in range(int(input())):
    x1, y1, x2, y2 = list(map(int, input().split()))
    cnt = 0
    for _ in range(int(input())):
        cx, cy, cr = map(int, input().split())
        d1 = (x1-cx)**2 + (y1-cy)**2
        d2 = (x2-cx)**2 + (y2-cy)**2
        pow_cr = cr**2
        
        if pow_cr > d1 and pow_cr > d2:
            continue
        elif pow_cr > d1 or pow_cr > d2:
            cnt += 1
    print(cnt)