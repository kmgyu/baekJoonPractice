from bisect import bisect_left

input = open(0).readline

def lis(arr):
    k = []
    l_k = []
    for i in range(N):
        idx = bisect_left(k, arr[i])
        if idx == len(k): k.append(arr[i])
        else: k[idx] = arr[i]
        l_k.append(idx+1)
    return max(l_k)

N = int(input())
A = list(map(int, input().split()))

print(N-lis(A))