import sys
input = sys.stdin.readline

n, k = map(int, input().split())

bags = []
for _ in range(n):
    bags.append(list(map(int, input().split())))
dp = [0]*(k+1)

for bag in bags:
    for j in range(k, bag[0]-1, -1):
        dp[j] = max(dp[j-bag[0]]+bag[1], dp[j])
print(dp[-1])
