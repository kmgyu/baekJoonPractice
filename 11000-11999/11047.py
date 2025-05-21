#11047
from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
coin = [int(input()) for i in range(n)]
coin.sort(reverse=True)
count = 0
for i in coin:
    count += k//i
    k %= i
print(count)