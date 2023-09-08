n = int(input())

dp = [0, 1]
for i in range(2, n+1):
    k = 1e9
    for j in range(1, int(i**0.5)+1):
        k = min(k, dp[i-j*j]+1)
    dp.append(k)
print(dp[-1])