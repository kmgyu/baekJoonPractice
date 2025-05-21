# 16198은 이걸 위해...
# 요세푸스처럼 최대 대칭 문자 개수 찾기하면 됨
# lr : l부터 r구간에서 대칭되는 문자의 최대 개수
# 점화식 구하는 게 중요할 듯
# for i in range(l+1, r):
#     dp[l][r] = max(dp[l][r], dp[l+1][r-1] + (dp[l]==dp[r]))

from collections import defaultdict

input = open(0).readline
# 16198 dp 풀이랑 유사함! 대신 좀 더 어렵다. 인덱싱 신경쓸 것?

N = int(input())
S = [*input()]
Q = int(input())

query = [map(int, input().split()) for _ in range(Q)]

matched = [[0]*N for _ in range(N)] # 매칭 체커
dp = [[0]*N for _ in range(N)] # 구간 최대값

for length in range(2, N+1, 2):
    for l in range(N - length + 1):
        r = l + length - 1 
        bias = S[l]==S[r] # r - l + 1에서 1 생략 후 부정논리연산 안씀
        matched[l][r] = bias + matched[l+1][r-1]

# 구간 최댓값은 여기서 구해야 한다.
for length in range(2, N+1):
    for l in range(N - length + 1):
        r = l + length - 1
        dp[l][r] = max(matched[l][r], dp[l][r-1], dp[l+1][r])


for l, r in query:
    print(dp[l-1][r-1])