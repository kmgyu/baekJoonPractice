import sys
N = int(input())

schedule = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

dp = [0 for i in range(N+1)]

for i in range(N):
    for j in range(i+schedule[i][0], N+1): #종료인덱스부터 N까지 접근
        if dp[j] < dp[i] + schedule[i][1]:
            dp[j] = dp[i] + schedule[i][1]

print(dp[-1])

# https://great-park.tistory.com/48