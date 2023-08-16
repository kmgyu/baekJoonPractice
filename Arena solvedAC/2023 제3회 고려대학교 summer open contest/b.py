from math import isqrt
n = int(input())
if isqrt((n))**2 == n: print(-1)
else:
    cnt = 0
    acnt = 0
    for i in range(1, isqrt(n)+1):
        a = (n-i**2)
        c = (n+i**2)
        if isqrt(a)**2 == a:
            acnt+=1
        if isqrt(c)**2 == c:
            cnt+=1
    for i in range(isqrt(n)+1, n):
        c = (n+i**2)
        if isqrt(c)**2 == c:
            cnt+=1
    print(cnt+acnt//2)