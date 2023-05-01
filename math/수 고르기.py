from sys import stdin
input = stdin.readline
N, K = map(int, input().split())
num = sorted(list(map(int, input().split())), reverse=True)
s = 0
for i in range(0,K):
    s+= num[i] - i
print(s)