from sys import stdin, stdout
input = stdin.readline
print = stdout.write
n, m = map(int, input().split())
nums = list(map(int,input().split()))
for i in range(1, len(nums)):
    nums[i] += nums[i-1]
for i in range(m):
    a, b = map(int, input().split())
    ss = nums[b-1]
    if a > 1:
        ss -= nums[a-2]
    print(str(ss)+"\n")
