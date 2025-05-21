def pow(n, a):
    if a == 0:return 1
    elif a == 1:return n
    ans = 1
    while a:
        if a % 2:
            ans = (ans*n) % mod
        a >>= 1
        n = n * n % mod
    return ans

n, r = map(int, input().split())
mod = 1000000007
fact = 1
f = [1]*3
for i in range(2, max(n, r)+1):
    fact = (fact*i)%mod
    if i == n:f[0] = fact
    if i == r:f[1] = fact
    if i == n-r:f[2] = fact

print(f[0] * pow(f[1] * f[2], mod-2) % mod)