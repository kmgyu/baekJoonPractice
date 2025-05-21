from bisect import bisect_left

input = open(0).readline

def lis(arr, N, start):
    k = [arr[start]]
    l_k = []
    for i in range(start+1, N):
        if arr[i] < k[0]: continue
        idx = bisect_left(k, arr[i])
        if idx == len(k): k.append(arr[i])
        else: k[idx] = arr[i]
        l_k.append(idx+1)
    return max(l_k) if l_k else 1

N = int(input())
arr = [int(input()) for _ in range(N)]
lis_l = [lis(arr, N, i) for i in range(N)]
drr = [-arr[i] for i in range(N)]
lds_l = [lis(drr, N, i) for i in range(N)]

ans = 0
for i in range(N): ans=max(ans, lis_l[i]+lds_l[i]-1)
print(ans)