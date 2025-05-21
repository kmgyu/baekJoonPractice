import sys
sys.setrecursionlimit(10**6)
A = {0:1}
n, p, q, x, y = map(int, input().split())
def find(num):
    if num <= 0:
        return 1
    if num not in A:
        A[num] = find(num//p-x)+find(num//q-y)
    return A[num]

print(find(n))