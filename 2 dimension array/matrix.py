r, c = map(int, input().split()) #row, column
A = list()
B = list()
for i in range(r):
    a = list(map(int, input().split()))
    A.append(a)
for i in range(r):
    a = list(map(int, input().split()))
    B.append(a)

for i in range(r):
    for j in range(c):
        A[i][j] += B[i][j]

for i in range(r):
    print(*A[i])
