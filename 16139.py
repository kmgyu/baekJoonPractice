import sys
input = sys.stdin.readline

s = input().rstrip()
n = int(input())

al = [[] for _ in range(26)]

for i in s:
    for j in range(26):
        if not al[j]: al[j].append(0)
        else: al[j].append(al[j][-1])
    al[ord(i)-97][-1] += 1

for i in range(n):
    a, l, r = input().split()
    l, r = int(l), int(r)
    alpha = ord(a)-97
    if l: print(al[alpha][r]-al[alpha][l-1])
    else: print(al[alpha][r])
