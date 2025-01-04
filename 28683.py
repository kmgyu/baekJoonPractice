from math import isqrt
n = int(input())
if isqrt((n))**2 == n: print(-1)
else:
    cnt = 0
    for i in range(1, (isqrt(n//2+1))+1):
        a = (n-i**2)
        if isqrt(a)**2 == a:
            cnt+=1
    for i in range(1, isqrt(n)+1):
        if n % i == 0:
            if (i + (n//i)) % 2 == 0:
                if i == n//i: continue
                cnt += 1
    print(cnt)

