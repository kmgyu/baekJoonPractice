from sys import stdin
input = stdin.readline
def binSearch(left, right, n):
    mid = (left+right)//2
    if left > right or mid >= len(nums):
        print(-1)
        return
    if nums[mid] == n:
        if right == mid:
            print(mid)
            return
        else: #lower bound
            binSearch(left, mid, n)
    elif nums[mid] < n:
        left = mid+1
        binSearch(left, right, n)
    else: #nums[mid] < n
        right = mid-1
        binSearch(left, right, n)


n,m = map(int, input().split())
nums = sorted([int(input()) for _ in range(n)])
for i in range(m):
    binSearch(0, n, int(input()))
