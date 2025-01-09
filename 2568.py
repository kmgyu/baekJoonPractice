from bisect import bisect_left

def lis(linked_port, sorted_port):
    # n log n LIS algorithm
    k = []
    l_k = []
    for i in sorted_port:
        idx = bisect_left(k, linked_port[i])
        if idx == len(k): k.append(linked_port[i])
        else: k[idx] = linked_port[i]
        l_k.append(idx+1)
    return l_k

input = open(0).readline
N = int(input())
linked_port = dict()

for i in range(N):
    a, b = map(int, input().split())
    linked_port[a] = b

sorted_port = sorted(linked_port.keys())
lcs_arr = lis(linked_port, sorted_port)
l_len = max(lcs_arr) # longest length
rm_cnt = N-l_len # need to remove
rm_arr = []

for i in range(N-1, -1, -1):
    if l_len == lcs_arr[i]: l_len -= 1
    else: rm_arr.append(sorted_port[i])
print(rm_cnt)
print(*sorted(rm_arr), sep="\n")