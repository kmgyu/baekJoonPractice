# 18185
# skyline을 40ms로 풀수있는 미친 정신나간 로직
from sys import stdin
input = stdin.readline
N = int(input())
A = list(map(int, input().rstrip().split())) + [0, 0]
answer = 0
for i in range(N):
    if A[i+1] > A[i+2]:
        cnt = min(A[i], A[i+1]-A[i+2])
        answer += cnt*5
        A[i] -= cnt
        A[i+1] -= cnt

        cnt = min(A[i], A[i+1], A[i+2])
        answer += cnt*7
        A[i] -= cnt
        A[i+1] -= cnt
        A[i+2] -= cnt
    else:
        cnt = min(A[i], A[i+1], A[i+2])
        answer += cnt*7
        A[i] -= cnt
        A[i+1] -= cnt
        A[i+2] -= cnt
    answer += A[i]*3
print(answer)
