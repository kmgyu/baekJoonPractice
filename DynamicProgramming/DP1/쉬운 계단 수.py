dp = [[0,1,1,1,1,1,1,1,1,1]]
n = int(input())
for i in range(1, n):
    temp = []
    temp.append(dp[i-1][1])
    for j in range(1,9):
        temp.append(dp[i-1][j-1]+dp[i-1][j+1])
    temp.append(dp[i-1][8])
    dp.append(temp)
print(sum(dp[n-1])%1000000000)