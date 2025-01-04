#9020
from sys import stdin, stdout
N = 1000001
li = [1]*N
arr = []
for i in range(2, 10001):
    if li[i] == 1:
        arr.append(i)
        for j in range(i+i, N, i):
            if li[j] == 1:
                li[j] = 0

for i in range(int(input())):
    n = int(stdin.readline())
    for i in arr:
        if li[i]==1 and li[n-i]==1 and n-i <= i:
            stdout.write(f"{n-i} {i}\n")
            break