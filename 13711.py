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

N = int(input())

# 전깃줄 문제와 유사하다. (그냥 같다고 보면 될듯)
# B는 같은 값이 A에서 어디에 위치하는지 찾아야 한다.
# A와 B 간의 링크를 만들어내면, 끊을 위치를 찾을 수 있다.
arr = []
A=dict()
for v, i in zip(map(int, input().split()), range(N)):
    A[v] = i
# A = {int(input()): i for i in range(N)}
B = [*map(int, input().split())]
for i in range(N): arr.append(A[B[i]])

A_lis = lis(arr, N)
print(A_lis)
