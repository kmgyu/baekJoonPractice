import math

n, p, v = map(int, input().split())
if n == 1:
    print(0)
else:
    d = 1
    time = n * p + v # base time
    for i in range(int(math.log2(n)) + 1): # solution보고 해석하자...
        d += 1
        m = int((n - 1) ** (1 / d)) #회의 멤버
        check = m ** d 
        time_check = d * (m * p + v)
        q = 0
        while check < n:
            check *= m + 1
            check //= m
            time_check += p
            q += 1
        time = min(time_check, time)
    print(time)
# https://jhhope1.tistory.com/24
# f(n) = f(ceil(n/k)) + f(k)로 쪼개진다는 점을 찾고 나면,
# 기본 식 f(m) = mP + V로 쓰는 k개 항 n=m1+m2+...mk으로
# 나눌 때 봐야 하는 k가 log n개밖에 없다는 사실을 이용해서
# 각각 k개로 나눌 때의 답을 구하면 된다.
# k개로 나눌 때 합의 최소는 곱이 일정하므로
# floor(sqrtk(n))<=x<=ceil(sqrtk(n))인 x들로만 표현하는 경우가 된다.
# 또한 ceil(log 2(10^15)) = 50인데 3^50은 long long을 초과하므로 주의.
