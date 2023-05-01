n = int(input())
nums = list(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(i):
        ans = max(nums[i]+nums[j], ans)
print(ans)

#길이 구하고 그거의 합구하는거임! 최고합!