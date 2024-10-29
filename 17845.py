import sys
input = sys.stdin.readline

n,k = map(int, input().split())

subject = []
for _ in range(k):
    i, t = map(int, input().split())
    subject.append((i,t))

dp = [0]*(n+1)

for i in range(k):
    for j in range(n, subject[i][1]-1, -1):
        dp[j] = max(dp[j], dp[j-subject[i][1]]+subject[i][0])

print(dp[-1])