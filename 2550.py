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

arr1 = [*map(int, input().split())]
arr2 = [*map(int, input().split())]

tmp_link = {arr2[i] : i for i in range(N)}

for i in range(N):
    linked_port[i] = tmp_link[arr1[i]]

sorted_port = sorted(linked_port.keys())
lcs_arr = lis(linked_port, sorted_port)
l_len = max(lcs_arr) # longest length
print(l_len)

l_arr = []
for i in range(N-1, -1, -1):
    if l_len == lcs_arr[i]:
        l_len -= 1
        l_arr.append(arr1[sorted_port[i]])
print(*sorted(l_arr))