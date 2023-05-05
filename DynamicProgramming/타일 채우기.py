#https://nahwasa.com/entry/%EB%B0%B1%EC%A4%80-2133-%EC%9E%90%EB%B0%94-%ED%83%80%EC%9D%BC-%EC%B1%84%EC%9A%B0%EA%B8%B0-BOJ-2133-JAVA

n = int(input())
dp = [1, 0, 3] + [0]*(n-2)
for i in range(4,n+1):
    dp[i] = dp[i-2] * 3
    for j in range(4, i+1, 2):
        dp[i] += dp[i-j] * 2
print(dp[n])