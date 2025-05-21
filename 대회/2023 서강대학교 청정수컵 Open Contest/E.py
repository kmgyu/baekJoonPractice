n = int(input())
# nums1 = list(range(1, n//2+1))
nums1 = list(range(n//2, 0, -1))
nums2 = list(range(n//2+1, n+1))
ans = []

for i in range(len(nums1)):
    ans.append(nums2.pop())
    ans.append(nums1.pop())
if nums2:
    ans.append(nums2.pop())
print(*ans)