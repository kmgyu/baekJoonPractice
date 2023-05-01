import sys
input = sys.stdin.readline
M,N = map(int, input().rstrip().split())
prime = []
arr = [False, False] + [True] * (N-1)
for i in range(2, N+1):
    if arr[i]:
        prime.append(i)
        for j in range(2*i, N+1, i):
            arr[j] = False
for i in prime:
    if i >= M:
        print(i)