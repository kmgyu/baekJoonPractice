#14002
from sys import stdin
input = stdin.readline
N = int(input())
A = [0]
dp = [0] * (N+1)
per = [[] for _ in range(N+1)]

A += list(map(int, input().split()))
for i in range(1, N+1): # 1 ~ N
    for j in range(i): # 0 ~ i-1
        # dp[i]는 A[i] 보다 작은 A[j] 중 가장 큰 dp[j] 값에 1을 더한 값이다.
        if A[i] > A[j]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j]+1
                per[i] = per[j] + [A[i]]
mIndex = dp.index(max(dp))
print(dp[mIndex])
print(*per[mIndex])