# refer : https://blog.naver.com/mym0404/222323009491
# 생각보다 좋은 문제였다.
# 복붙 시에 대한 연관성을 이런식으로 증명해야 한다...!

N = int(input())

dp = [*range(6)]

for i in range(6, N+1):
    ret = 0
    # A 입력
    ret = max(ret, dp[i-1]+1)
    # 바로 K 복붙
    ret = max(ret, dp[i-3]*2)
    # K 복붙 두번
    ret = max(ret, dp[i-4]*3)
    # K 복붙 세번
    ret = max(ret, dp[i-5]*4)
    dp.append(ret)
print(dp[N])