import sys
input = sys.stdin.readline

n = int(input())
nums = []
for i in range(n):
    nums.append((int(input()), i))

nums.sort()

ans = 0
for i in range(n):
    ans = max(ans, nums[i][1] - i)
print(ans+1)