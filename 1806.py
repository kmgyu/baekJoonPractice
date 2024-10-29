n, s = map(int, input().split())
nums = list(map(int, input().split()))

left, right = 0, 0
res = nums[0]
ans = 10e9

while True:
    if res < s:
        right += 1
        if right == n: break
        res += nums[right]
    else:
        res -= nums[left]
        ans = min(ans, right-left+1)
        left += 1
print(ans if ans != 10e9 else 0)