n = int(input())
nums = list(range(1,n+1))
ans = 0
for i in range(1,n):
    ans += i*(n-i)
print(ans)
for i in range(n-1):
    print(nums[i], nums[i+1])
