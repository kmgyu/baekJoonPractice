# https://wooono.tistory.com/605
# 문제간의 연관관계.. 그아아

N, M = map(int, input().split())
terrain = [[*map(int, input().split())] for _ in range(N)]

# 초기 : 왼쪽부터 오른쪽 확정
dp = [terrain[0][0]]
for i in range(1, M):
    dp.append(dp[-1] + terrain[0][i])

for i in range(1, N):
    # 이동 방향 : left, right
    tmp_left = terrain[i][:]
    tmp_right = terrain[i][:]
    tmp_left[0] += dp[0]
    tmp_right[-1] += dp[-1]
    # 아래랑 이동방향 비교하여 더할 때 더 큰값을 더해줌.
    for j in range(1, M):
        tmp_left[j] += max(tmp_left[j-1], dp[j])
        tmp_right[M-j-1] += max(tmp_right[M-j], dp[M-j-1])
    # 대소 비교하여 최종적으로 큰값을 비교한다.
    # 좌우 간에...
    for j in range(M): dp[j] = max(tmp_left[j], tmp_right[j])
print(dp[-1])
