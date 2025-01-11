import sys
from math import gcd
input = sys.stdin.readline
# greedy
N, K = map(int, input().split())
A = [*map(int, input().split())]
step = gcd(N, N-K)

if step>1:
    for i in range(N):
        if A[i]%step != i%step:
            print('NO')
            break
    else:
        print('YES')
else:
    print('YES')
# if (N%2 or K%2) and N%K:
#     print('YES')
# elif N%K == 0:
#     for i in range(N):
#         if A[i]%K != i%K:
#             print('NO')
#             break
#     else:
#         print('YES')
# else:
#     for i in range(N):
#         if A[i]%2 != i%2:
#             print('NO')
#             break
#     else:
#         print('YES')

print(set((i*K)%N for i in range(N)))
print(step)