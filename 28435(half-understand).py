import sys
input = sys.stdin.readline
# 뇌 터질 거같음
# https://solved.ac/arena/1/editorial
# what the fuuuuuuckk
def pow(a, b, mod):
    if b == 0:
        return 1
    if b % 2:
        return a * pow(a, b-1, mod) % mod
    half = pow(a, b//2, mod)
    return half * half % mod

N, K = map(int, input().split())
MOD = 10**9 + 7

nums = list(map(int, input().split()))
c = [0]*K

for num in nums:
    c[num%K] += 1

ans = 1
for i in range(1, (K+1)//2):
    ans = ans * (pow(2, c[i], MOD) + pow(2, c[K-i], MOD) - 1) % MOD

ans = ans * (c[0] + 1) % MOD
if K%2 == 0:
    ans = ans*(c[K//2]+1) % MOD
ans = (ans - (N+1)) % MOD
print(ans)