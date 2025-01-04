#17103
from sys import stdin, stdout
N = 1000001
li = [1]*N
for i in range(2, 1001):
    if li[i] == 1:
        for j in range(i+i, N, i):
            if li[j] == 1:
                li[j] = 0
input = stdin.readline
for i in range(int(input())):
    num = int(input())
    count = 0
    for j in range(2, num//2+1):
        if li[j] and li[num-j]:
            count+=1
    print(count)