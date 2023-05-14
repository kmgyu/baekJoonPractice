#RGB거리와 조건은 같지만, 원형인 문제로 생각하면 된다.
#1번과 n번의 색깔이 달라야 하기 때문에.
from sys import stdin
import copy
input = stdin.readline
n = int(input())
rgb = []
for i in range(n):
    rgb.append(list(map(int, input().split())))

ans = 10e9
for k in range(3):
    dp = copy.deepcopy(rgb)
    for i in range(3):
        if i != k:
            dp[0][i] = 10e9
    for i in range(1, n):
        for j in range(3):
            dp[i][j] += min(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])
    for i in range(3):
        if i == k: continue
        ans = min(dp[-1][i], ans)
print(ans)