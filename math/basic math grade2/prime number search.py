from math import *
N = int(input())
num = list(map(int, input().split()))
count = 0
for num in num:
    i = int(sqrt(num)) + 1
    if num == 1:
        count += 1
        continue

    for k in range(2, i):
        if num % k == 0:
            count += 1
            break;
print(N-count)