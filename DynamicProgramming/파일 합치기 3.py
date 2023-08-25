import sys
from heapq import heappush, heappop
input = sys.stdin.readline

t = int(input())
for i in range(t):
    k = int(input())
    n = list(map(int, input().split()))
    nums = []
    for i in n:
        heappush(nums, i)
    result = 0
    while True:
        a = heappop(nums)
        if nums:
            b = heappop(nums)
        else:
            break
        heappush(nums, a+b)
        result += a+b
    print(result)