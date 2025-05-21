# https://deveun.tistory.com/entry/Python%EB%B0%B1%EC%A4%80-11062%EC%B9%B4%EB%93%9C%EA%B2%8C%EC%9E%84

input = open(0).readline
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    dp = [[0 for _ in range(N)] for _ in range(N)]
    # 여기서 사용한 dp는 게임이론을 응용한 것이다. 아아ㅏㅇ가가악ㄱ가각
    # 근우차례 : 선택할 카드 및 다음 선택 카드합이 최대
    # 명우차례 : 선택할 카드 및 남은 카드들로 근우가 선택할 카드합이 최소
    # 끼에에에ㅔ게ㅔㅇ겡게ㅔㅇ겡ㄱㅇㄱㅇ겡겍!!!!!!!!!!

    turn = True if N % 2 == 1 else False # True일 때 근우차례

    for j in range(N):
        for i in range(N - j):
            if j == 0:
                dp[i][i+j] = arr[i] if turn else 0
            elif turn: #근우차례
                dp[i][i+j] = max(dp[i+1][i+j] + arr[i], dp[i][i+j-1] + arr[i+j])
            else: #명우차례
                dp[i][i+j] = min(dp[i+1][i+j], dp[i][i+j-1])
        turn = not turn

    print(dp[0][N-1])