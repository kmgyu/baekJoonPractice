from sys import stdin
input = stdin.readline
N = int(input())
A = [0]
dp = [0] * (N+5)
A += list(map(int, input().split()))
for i in range(1, N+1):
    for j in range(i):
        if A[i] < A[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp)+1)

# short code. much to learn
# 파일을 읽어와 스플릿하고, 1001까지 범위를 저장해 본인 위에 있는거의 최댓값+1해주는 거임... 개쩐다.
# d=[0]*1002
# for i in map(int,[*open(0)][1].split()):d[i]=max(d[i+1:])+1
# print(max(d))
