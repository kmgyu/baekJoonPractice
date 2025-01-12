input = open(0).readline
N, P = map(int, input().split())
for i in range(N): input()
bound = N//3
l, r = bound, N-bound-(N%3==2)
if l<=P<=r: print('YES')
else: print('NO')