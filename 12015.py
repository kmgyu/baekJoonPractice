# https://velog.io/@uoayop/BOJ-12015-%EA%B0%80%EC%9E%A5-%EA%B8%B4-%EC%A6%9D%EA%B0%80%ED%95%98%EB%8A%94-%EB%B6%80%EB%B6%84-%EC%88%98%EC%97%B4-2-Python

import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().rsplit()))
seq = []
ans = 0

for num in a:
    if not seq:
        seq.append(num)
        ans += 1
        continue
    if seq[-1] < num:
        seq.append(num)
        ans += 1
    else:
        index = bisect_left(seq, num)
        seq[index] = num
print(ans)