from bisect import bisect_left

input = open(0).readline

def lis(arr, N):
    k = []
    l_k = []
    for i in range(N):
        idx = bisect_left(k, arr[i])
        if idx == len(k): k.append(arr[i])
        else: k[idx] = arr[i]
        l_k.append(idx+1)
    return max(l_k)

def lds(arr, N):
    k = []
    l_k = []
    drr = [-arr[i] for i in range(N)]
    for i in range(N):
        idx = bisect_left(k, drr[i])
        if idx == len(k): k.append(drr[i])
        else: k[idx] = drr[i]
        l_k.append(idx+1)
    return max(l_k)

N = int(input())
# arr = [int(input()) for _ in range(N)]
arr = [*map(int, input().split())]
print(max(lis(arr, N), lds(arr, N)))
