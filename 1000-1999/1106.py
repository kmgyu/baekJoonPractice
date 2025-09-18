# https://bio-info.tistory.com/218
# 다 까먹었다... 이걸로 dp 연습이라도 하자...

import sys
input = sys.stdin.readline

C,N = map(int,input().split())
hotel = [list(map(int,input().split())) for _ in range(N)]
dp = [float('inf') for _ in range(max(C, 101))]
dp[0]=0
for cost, num_people in hotel:
    for i in range(num_people,max(C, 101)):
        dp[i] = min(dp[i-num_people]+cost,dp[i])

print(min(dp[C:]))