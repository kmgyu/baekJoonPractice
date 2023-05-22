from sys import stdin
input = stdin.readline
N = int(input())
A = [0]
dp = [0] * (N+5)
A += list(map(int, input().split()))
for i in range(1, N+1):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp)+1)