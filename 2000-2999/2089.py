from math import ceil
n = int(input())
b = -2
ans = ''
if n == 0:
    print(n)
else:
    while n:
        ans += str(abs(n % b))
        n = int(ceil(n/-2))
    ans = list(reversed(ans))
    print(*ans, sep="")

