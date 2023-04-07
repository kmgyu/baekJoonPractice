#2798
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
num = list(map(int, input().split()))

l = len(num)
num_s = set()
for i in range(0, l):
    for j in range(1, l):
        for k in range(2, l):
            if i==j or i==k or j==k :
                continue
            else :
                num_s.add(num[i]+num[j]+num[k])

num_s = list(num_s)

find = list()
for i in range(0, len(num_s)):
    if (num_s[i] - m) > 0 : continue
    find.append(abs(num_s[i] - m))
print(m-min(find))

