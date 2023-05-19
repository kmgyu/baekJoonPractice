nums = [1, 4, 5, 8, 15, 16, 17, 18, 19, 21, 22, 24, 26, 27, 28, 31, 37, 40, 44, 45, 47, 48, 50, 51, 57, 58, 59, 60, 61, 62, 65, 68, 69, 71, 72, 73, 76, 78, 79, 81, 82, 83, 85, 86, 88, 92, 94, 98, 99, 100]
#question list
leng = len(nums)
#2차원 누적합.
def cumsum(n, m): #1번문제
    dp = [0, nums[0]]
    for i in range(1, m):
        dp.append(nums[i]+dp[-1])
    print(dp[m]-dp[n])

def finder(n): #2번문제
    for i in range(leng):
        for j in range(i+1, leng):
            if nums[i] + nums[j] == n:
                print(i, j)
                return
    print(-1)

# cumsum(4, 8)
finder(int(input()))