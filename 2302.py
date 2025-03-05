import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
l1 = [0] + [int(input()) for _ in range(m)]
if l1[-1] != n: l1 += [n+1]
l2 = [l1[i] - l1[i-1] -1 for i in range(1, len(l1))]
dp = [1,2]
for i in range(1, max(l2)):
    dp.append(dp[i]+dp[i-1])
ans = 1
for i in l2:
    if i == 0: continue
    ans *= dp[i-1]
print(ans)