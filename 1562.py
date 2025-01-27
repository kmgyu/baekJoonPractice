# refer : https://velog.io/@js43o/%EB%B0%B1%EC%A4%80-1562%EB%B2%88-%EA%B3%84%EB%8B%A8-%EC%88%98

input = open(0).readline

N = int(input())
dp = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(N)]
# 1024의 경우 0, 9를 포함하는 경우 4개로 최적화 가능하다.
# 근데 이게 뭐야 아러이ㅏ러ㅏ민얼;ㅣㅏㅁㄴ어;리ㅏㄴ머;이라
# 어케했노 ㅅㅂ
mod = 10 ** 9
res = 0

for k in range(1, 10):
    dp[0][k][1 << k] = 1

for i in range(1, N):
    for k in range(10):
        for bit in range(1024):
            if k - 1 >= 0: dp[i][k][bit | (1 << k)] += dp[i - 1][k - 1][bit]
            if k + 1 <= 9: dp[i][k][bit | (1 << k)] += dp[i - 1][k + 1][bit]
            dp[i][k][bit | (1 << k)] %= mod

for k in range(10):
    res += dp[N - 1][k][1023]
    res %= mod

print(res)