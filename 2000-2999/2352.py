from bisect import bisect_left

def lis(arr, N):
    # n log n LIS algorithm
    k = []
    l_k = []
    for i in range(N):
        idx = bisect_left(k, arr[i])
        if idx == len(k): k.append(arr[i])
        else: k[idx] = arr[i]
        l_k.append(idx+1)
    return l_k

input = open(0).readline
N = int(input())
port = [*map(int, input().split())]

ans = max(lis(port, N))
print(ans)