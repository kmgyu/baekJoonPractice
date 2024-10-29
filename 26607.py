import sys
input = sys.stdin.readline
n, k, x = map(int, input().split())
dp = [set() for _ in range(k+1)]
dp[0].add(0)
bag = []
for i in range(n):
    a,b = map(int, input().split())
    bag.append(a)

for i in bag:
    for j in range(k, 0, -1):
        for l in dp[j-1]:
            dp[j].add(l + i)

print(max(i*(k*x-i) for i in dp[-1]))