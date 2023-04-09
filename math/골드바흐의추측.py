#6588
from sys import stdin, stdout
N = 1000001
li = [1]*N
arr = []
for i in range(2, 1001):
    if li[i] == 1:
        arr.append(i)
        for j in range(i+i, N, i):
            if li[j] == 1:
                li[j] = 0

while True:
    n = int(stdin.readline())
    if n == 0:
        break
    for i in arr:
        if li[i]==1 and li[n-i]==1:
            stdout.write(f"{n} = {i} + {n-i}\n")
            break