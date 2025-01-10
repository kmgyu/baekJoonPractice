input = open(0).readline

N = int(input())
arr = sorted(map(int, input().split()))
MOD = 10**9 + 7

pows = {i: pow(2, i, MOD) for i in range(N)}
ans = 0
for i in range(N):
    tmp = pows[i] - pows[N-i-1]
    tmp*=arr[i]
    ans = (ans+tmp)%MOD
print(ans)