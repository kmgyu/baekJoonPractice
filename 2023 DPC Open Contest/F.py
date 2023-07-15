mod = 1000000007

def pow(n, a):
    if a == 1:
        return n % mod
    if a % 2 == 1:
        b = pow(n, a//2)
        return (b*b*n) % mod
    b = pow(n, a//2)
    return b*b

n, a = map(int, input().split())
b = pow(n, a+1)
c = pow(n-1, a)
ans = (n-2)*(b-c*n)+b
ans %= mod
print(ans)