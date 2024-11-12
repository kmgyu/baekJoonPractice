from bisect import bisect_left

input = open(0).readline

def lis(arr):
    k = []
    l_k = []
    for i in range(n):
        idx = bisect_left(k, arr[i])
        # if idx == len(k):
        if idx == len(k): k.append(arr[i])
        else: k[idx] = arr[i]
        l_k.append(idx+1)
        
    return l_k


n=int(input())
A = list(map(int, input().split()))
tmp = 0
l_k = lis(A)
max_l = max(l_k)
print(max_l)
ans = []
for i in range(n-1, -1, -1):
    if max_l == l_k[i]:
        max_l -= 1
        ans.append(A[i])
print(*ans[::-1])