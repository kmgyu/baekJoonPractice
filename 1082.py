N = int(input())
P = [*map(int,input().split())]
M = int(input())

answer = [0]

if len(P) > 1 and min(P[1:]) <= M:
    # 첫번째 숫자 정하기
    cost = M
    for i in range(1, N):
        if P[i] == min(P[1:]):
            answer[0] = i
            cost = M-P[i]

    # 이후 자릿수 가장 많이 채우기
    target = 0
    for i in range(N):
        if P[i] == min(P):
            target = i

    for i in range(cost//P[target]):
        answer.append(target)

    cost %= P[target]


    length = len(answer)


    idx = 0
    while idx < length and cost > 0:
        # 현재 가격비교해서 가능한 수 중 가장 높은 수
        current = answer[idx]
        change = answer[idx]
        for i in range(current+1, N):
            if P[i] - P[current] <= cost:
                change = i
        
        answer[idx] = change
        cost -= P[change] - P[current]
        
        idx += 1

print(*answer, sep="")