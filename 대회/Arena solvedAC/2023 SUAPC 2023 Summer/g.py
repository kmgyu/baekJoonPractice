import sys
input = sys.stdin.readline
n = int(input())
P = list(map(int, input().split()))
T = [[] for _ in range(5)]
for i in range(n):
    k, t = map(int, input().split())
    T[k-1].append(t)

for i in range(5):
    T[i].sort()
ans = 0
for i in range(5):
    for j in range(P[i]):
        ans += T[i][j]
        if j > 0:
            ans += T[i][j]-T[i][j-1]
    ans +=60
print(ans-60)