from collections import Counter
from sys import stdin
input = stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums[0] %= m
for i in range(1, n):
    nums[i] = (nums[i] + nums[i-1])%m
cnt = Counter(nums)
ans = cnt[0]
for i in cnt.values():
    ans += int(i * (i-1)/2)
#cnt의 길이는 나머지의 길이이다... 즉 m과같다.
print(ans)
