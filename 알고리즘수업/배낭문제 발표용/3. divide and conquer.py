def knapsack_dc(W, wt, val, n):
    '''
    W = 배낭의 무게
    wt = 물건의 무게(리스트)
    val = 물건의 가치(리스트)
    n = 물건의 개수
    '''
    if n==0 or W==0:
        # 기반상황
        # 물건이 없거나 배낭의 무게가 0이면 0을 반환한다.
        return 0
    
    if (wt[n-1] > W):
        # 현재 물건의 무게가 배낭의 무게보다 크다면
        return knapsack_dc(W, wt, val, n-1) # 현재 물건을 고려 대상에서 제외
    else:
        valWith = val[n-1] + knapsack_dc(W-wt[n-1], wt, val, n-1) # 현재 물건을 넣은 경우
        valWithout = knapsack_dc(W, wt, val, n-1) # 현재 물건을 넣지 않은 경우(고려 대상에서 제외)
        return max(valWith, valWithout) # 두 경우를 비교해, 가치가 더 높은 쪽을 선택
