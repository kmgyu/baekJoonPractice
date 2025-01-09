from bisect import bisect_left

input = open(0).readline

def lis(dict_arr, sorted_arr):
    # n log n LIS algorithm
    k = []
    l_k = []
    for i in sorted_arr:
        idx = bisect_left(k, dict_arr[i])
        if idx == len(k): k.append(dict_arr[i])
        else: k[idx] = dict_arr[i]
        l_k.append(idx+1)
    return max(l_k)

T = int(input())

for _ in range(T):
    N = int(input())
    K = {i:int(input()) for i in range(N)}
    sorted_K = sorted(K.keys())
    print(lis(K, sorted_K))