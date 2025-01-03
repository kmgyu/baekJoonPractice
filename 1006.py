T = int(input())

for _ in range(T):
    N, W = map(int, input().split())
    enemy = [list(map(int, input().split())) for _ in range(2)]
    S = [[0] * N for _ in range(3)]
    S[0].append(0)
    res = float('inf')
    
    def solve(start):
        # 1*2, 2*1, 2*2 타일링 문제와 유사. (케이스 이해가 잘 안되는데 이거 맞으려나)
        for i in range(start, N):
            S[0][i+1] = min(S[1][i]+1, S[2][i]+1)
            if enemy[0][i] + enemy[1][i] <= W: # 기본, 1*1 타일링
                S[0][i+1] = min(S[0][i+1], S[0][i]+1)
            if (i>0) and (enemy[0][i-1] + enemy[0][i] <= W) \
                and enemy[1][i-1] + enemy[1][i] <= W: # 1*2 타일링
                    S[0][i+1] = min(S[0][i+1], S[0][i-1] + 2)
            if i < N-1: # 2*1 타일링, N-1인 이유는 환형이라 케이스 구분해야되서.
                S[1][i+1] = S[0][i+1] + 1
                if enemy[0][i] + enemy[0][i+1] <= W:
                    S[1][i+1] = min(S[1][i+1], S[2][i] + 1)
                S[2][i+1] = S[0][i+1] + 1
                if enemy[1][i] + enemy[1][i+1] <= W:
                    S[2][i+1] = min(S[2][i+1], S[1][i] + 1)
    
    S[1][0], S[2][0] = 1, 1
    solve(0)
    res = min(res, S[0][-1])
    # 환형인 점에 따른 케이스 분류
    if N>1:
        if enemy[0][0] + enemy[0][-1] <= W: # case 1 : 1*2가 들어오는 경우
            S[0][1] = 1
            S[1][1] = 2
            S[2][1] = 1 if enemy[1][0] + enemy[1][1] <= W else 2
            solve(1)
            res = min(res, S[2][-1]+1)
        if enemy[1][0] + enemy[1][-1] <= W: # case 2 : 2*1이 들어오는 경우
            S[0][1] = 1
            S[1][1] = 1 if enemy[0][0] + enemy[0][1] <= W else 2
            S[2][1] = 2
            solve(1)
            res = min(res, S[1][-1]+1)
        if enemy[0][0] + enemy[0][-1] <= W and enemy[1][0] + enemy[1][-1] <= W: # case 3 : 2*2가 들어오는 경우 (맞나?)
            S[0][1] = 0
            S[1][1], S[2][1] = 1, 1
            solve(1)
            res = min(res, S[0][-2]+2)
    print(res)