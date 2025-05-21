#11054
from sys import stdin
input = stdin.readline
N = int(input())
A = [0] + list(map(int, input().split()))
dp1 = [0] * (N+1)
dp2 = [0] * (N+1)
ans = 0
for i in range(1, N+1):
    for j in range(i):
        if A[i] > A[j]:
            dp1[i] = max(dp1[j]+1, dp1[i])
for i in range(N, 0, -1):
    for j in range(N, i-1, -1):
        if A[i] > A[j]:
            dp2[i] = max(dp2[j]+1, dp2[i])
    ans = max(dp1[i]+dp2[i], ans)
print(ans)