import sys
sys.setrecursionlimit(10**9+1)

def koch(n, a):
    global mod
    ans = 1
    for i in range(1, a+1):
        length = pow(n, i-1, mod)
        ans = ((n-1) * (ans + length))%mod
    return ans

mod = 1000000007
n, a = map(int, input().split())

print(koch(n,a)*n%mod)