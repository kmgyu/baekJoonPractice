from collections import deque
import math
#A->B 16953
#probably DP.
a, b = map(int, input().split())
dp = dict()
dp[a] = 0
q = deque([a])
while q:
    temp = q.popleft()
    if temp*2 < b+1:
        dp[temp*2] = dp[temp]+1
        q.append(temp*2)
    if temp*10+1 < b+1:
        dp[temp*10+1] = dp[temp]+1
        q.append(temp*10+1)
try:
    print(dp[b]+1)
except:
    print(-1)

# 사실 이렇게 간단한 문제였다...
# A,B=map(int, input().split())
# count=1

# while A<B:
#     if B%2==0:
#         B=B//2
#     elif B%10 ==1:
#         B=B//10
#     else:
#         break
#     count+=1

# if A==B:
#     print(count)
# else:
#     print(-1)