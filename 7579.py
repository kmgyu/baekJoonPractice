import sys
input = sys.stdin.readline

n, m = map(int, input().split())
app1 = list(map(int, input().split()))
app2 = list(map(int, input().split()))

k = sum(app2)+1
dp = [0 for _ in range(k)]

for i in range(n):
    for j in range(k-1, -1, -1):
        if app2[i] > j: break
        dp[j] = max(app1[i] + dp[max(0, j-app2[i])], dp[j])

for i in range(k):
    if dp[i] >= m:
        print(i)
        break