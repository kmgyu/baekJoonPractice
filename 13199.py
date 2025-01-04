import sys
input = sys.stdin.readline

for i in range(int(input())):
    p, m, f, c = map(int, input().split())
    coupon = (m//p)*c
    cnt = 0
    if coupon >= f:
        cnt += (coupon - f)//(f-c) + 1
    print(cnt - (m//p)*c//f)