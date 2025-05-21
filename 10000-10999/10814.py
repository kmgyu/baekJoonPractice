import sys
input = sys.stdin.readline
n = int(input())
age_li = list()
for i in range(n):
    age, name = input().split()
    age_li.append([int(age), name])
age_li.sort(key=lambda x:x[0])
for i in age_li:
    print(*i)