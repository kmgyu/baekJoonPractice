# dp. 조합 최적화 문제 (최소화)
# 어떻게 최소 조합을 찾을 것인지 생각해보자.
# N*M, M*K의 행렬곱이 N*K. N*M*K 값을 비교해서 N*K 기대치 비교?
# 순서는 어떻게 할까? 링크드 리스트 형태로 만들고 합치기?
# https://one-way-people.tistory.com/38
# 대가리 박살
# 쥰내 어렵네

input = open(0).readline
N = int(input())
A = [list(map(int, input().split())) for _ in range(N)] # matrix
dp = [[float('inf')]*N for _ in range(N)] # dp matrix

for i in range(N): dp[i][i] = 0

# for loop가 i~j에 대한 기준으로 생성된다. term을 늘려가는 것이 기준이 되어야 한다?
# for i in range(N):
#     for j in range(i+1, N):
#         if i-j == 1: dp[i][j] = A[i][0] * A[i][1] * A[j][1]
#         else:
#             # i와 j 사이에 k로 분할하여 단계적으로 최솟값 탐색
#             for k in range(i, j):
#                 dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + A[i][0]*A[k][1]*A[j][1])

# term으로 두개의 행렬 N*M과 M*K로 분리한다.
# 그 사이에서 k라는 변수를 두어 최솟값 탐색
for term in range(1, N):
    for i in range(N-term):
        j = i + term
        if i-j == 1: dp[i][j] = A[i][0] * A[i][1] * A[j][1]
        else:
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + A[i][0]*A[k][1]*A[j][1])

print(dp[0][-1])