#1931번
from sys import stdin
input = stdin.readline

n = int(input())
num = []
for i in range(n):
    num.append(list(map(int, input().split())))
num.sort(key=lambda x : x[0])
num.sort(key=lambda x : x[1]) #종료시간 기준 배열

time = 0
count = 0
for i in num:
    if time == 0 or i[0] >= time:
        count+=1
        time = i[1]
print(count)