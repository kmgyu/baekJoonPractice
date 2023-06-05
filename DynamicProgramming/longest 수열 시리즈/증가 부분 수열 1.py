#11053
from sys import stdin
input = stdin.readline
N = int(input())
A = [0]
dp = [0] * (N+5)
A += list(map(int, input().split()))
for i in range(1, N+1): # 1 ~ N
    for j in range(i): # 0 ~ i-1
        # dp[i]는 A[i] 보다 작은 A[j] 중 가장 큰 dp[j] 값에 1을 더한 값이다.
        if A[i] > A[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))