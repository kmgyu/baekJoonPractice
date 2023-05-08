import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
num2 = sorted(set(nums))
ele = {num2[i]:i for i in range(len(num2))}
for i in range(n):
    print(ele[nums[i]], sep=" ")