# https://d-cron.tistory.com/23
from sys import stdin
input = stdin.readline
T = int(input())
#knapsack problem
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0]*(M+1)
    dp[0] = 1 #일단 0원을 만들 수 있는 가지수를 1로 초기화시킨다.
    # 어떤 동전이든 0원을 만들 수 있는 '가지수'는 무조건 1가지 존재한다는 의미
    for coin in coins:
        for i in range(1, M+1):
            if i >= coin:
                dp[i] += dp[i-coin]
    print(dp[M])