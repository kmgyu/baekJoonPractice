N = int(input())
W = [*map(int, input().split())]
# 1 < x < N 이라 할 때, W[x-1] * W[x+1]을 구하는 문제
# 하나의 원소에 대하여... dp로 풀 수 있다.
# https://gall.dcinside.com/mgallery/board/view/?id=ps&no=52961&page=1
# 진짜 미쳐버린듯 어케 이런걸 생각하는거임??

# dp[l][r] := l과 r 사이 (l < i < r)의 구슬들만 남아있다고 가정할 때, 그 사이에서 얻을 수 있는 최대 에너지

dp = [[0]*N for _ in range(N)]

for length in range(3, N+1):
    for l in range(N - length + 1): # 왼쪽 구간 포인터
        r = l + length - 1 # 오른쪽 구간 포인터
        for i in range(l+1, r):
            # i번째 인자를 마지막으로 제거한다고 가정한다. -> 마지막으로 남는건 l, r
            # [l][i] + [i][r] => 구간 이어주기.
            # 왼쪽부터 오른쪽으로 훑고 지나가면서 l~r 구간 계산해서 최댓값 구해준다.
            # 만약 중간에 0, N-1번보다 큰 값이 생겨서 구간이 분할된다? 그럼 재귀적으로 최댓값이 갱신된다.
            # 구간 분할 -> 최댓값 갱신 -> 재귀적 적용
            dp[l][r] = max(dp[l][r], dp[l][i] + dp[i][r] + W[l]*W[r])
print(dp[0][N-1])