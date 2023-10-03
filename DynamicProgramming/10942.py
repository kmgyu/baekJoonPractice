#팰린드롬? 10942
import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

pel = [[0]*n for _ in range(n)]

for i in range(n):
    pel[i][i] = 1
    if i < n-1 and nums[i] == nums[i+1]:
        pel[i][i+1] = 1

for continue_n in range(3, n+1):
    for start in range(n-continue_n + 1):
        end = start + continue_n - 1
        if nums[start] == nums[end] and pel[start+1][end-1]:
            pel[start][end] = 1

m = int(input())
for i in range(m):
    s, e = map(int, input().split())
    print(pel[s-1][e-1])