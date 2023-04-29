# https://gdlovehush.tistory.com/260
from sys import stdin
input = stdin.readline
ques = []
mod = 1000000009
dp = [[1,0,0], [0, 1, 0], [1, 1, 1]]
t = int(input())
for i in range(t):
    ques.append(int(input()))
for i in range(3, max(ques)):
    dp.append([dp[i-1][1] + dp[i-1][2], dp[i-2][0] + dp[i-2][2], dp[i-3][1] + dp[i-3][0]])
    for k in range(3):
        dp[i][k] %= mod
for k in ques:
    print(sum(dp[k-1])%mod)