from itertools import count
import sys
def input(): return sys.stdin.readline().rstrip()

n = int(input())
nums = list(map(int, input().split()))
q = int(input())
lNums = list(map(int, input().split()))

mx = max(max(nums), max(lNums))
dp = [0] * (mx+1)
for a in nums:
    dp[a] += 1

for i in range(2, mx+1):
    for j in count(1):
        if j*j > i: break
        if i % j == 0:
            dp[i] += dp[j]
            if j*j != i and j != 1:
                dp[i] += dp[i//j]

print(*(dp[i] for i in lNums))
# 해설에 적힌 코드. 엄청난 테크닉이다...!