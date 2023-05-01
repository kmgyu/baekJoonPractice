# 18185
from sys import stdin
input = stdin.readline
N, B, C = map(int, input().split())
A = list(map(int, input().rstrip().split())) + [0, 0]
answer = 0
bc1 = B+C
bc2 = B+2*C
if B > C:
    for i in range(N):
        
        if A[i+1] > A[i+2]:
            cnt = min(A[i], A[i+1]-A[i+2])
            answer += cnt*bc1
            A[i] -= cnt
            A[i+1] -= cnt

            cnt = min(A[i], A[i+1], A[i+2])
            answer += cnt*bc2
            A[i] -= cnt
            A[i+1] -= cnt
            A[i+2] -= cnt
        else:
            cnt = min(A[i], A[i+1], A[i+2])
            answer += cnt*bc2
            A[i] -= cnt
            A[i+1] -= cnt
            A[i+2] -= cnt
        answer += A[i]*B
else:
    for i in range(N):
        answer += A[i]*B
print(answer)
