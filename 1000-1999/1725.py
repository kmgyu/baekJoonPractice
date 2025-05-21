from sys import stdin
from collections import deque
input = stdin.readline
n = int(input())
nums = [0]
for i in range(n):
    nums.append(int(input()))
nums += [0]
s = [0] #stack
ans = 0
for i in range(1, n+2):
    while s and nums[s[-1]] > nums[i]:
        check = s.pop()
        ans = max(ans, nums[check]*(i-s[-1]-1))
    s.append(i)
print(ans)
#개쩌는 로직이다.....
# https://cocoon1787.tistory.com/315