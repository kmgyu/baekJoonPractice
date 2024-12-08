def knapsack_bb(obj, W, level, weight, profit, maxProfit):
    if (level == len(obj)): # 모두 탐색한 경우(단말 노드까지 처리함)
        return maxProfit # 지금까지 계산한 최대가치 반환
    
    # 무게를 넘지 않는 경우, 물건을 넣는 시도
    if weight + obj[level][0] <= W:
        newWeight = weight + obj[level][0]
        newProfit = profit + obj[level][1]
        maxProfit = max(newProfit, maxProfit) # 최대가치 갱신
        
        newBound = bound(obj, W, level+1, newWeight, newProfit) # 한계합 계산
        if newBound > maxProfit:
            maxProfit = knapsack_bb(obj, W, level+1, newWeight, newProfit, maxProfit) # 최대가치 계산(갱신)
        
    # 물건을 넣지 않은 경우에 대한 시도
    newWeight = weight
    newProfit = profit
    newBound = bound(obj, W, level+1, newWeight, newProfit)
    if newBound >= maxProfit: # 한계합 >= 최대가치 : 탐색할 가치가 있음!
        maxProfit = knapsack_bb(obj, W, level+1, newWeight, newProfit, maxProfit)
    
    return maxProfit


def bound(obj, W, level, weight, profit):
    # 분기한정시 한계합 계산
    if weight > W: # 무게 초과
        return 0
    
    pBound = profit # 현재까지 확정된 이익
    for j in range(level+1, len(obj)): # 아직 결정하지 않은 모든 물건의 가치합
        pBound += obj[j][1]
    
    return pBound

def bound2(obj, W, level, weight, profit):
    # 더 효율적인 분기한정시의 한계합 계산 방법
    if weight > W:
        return 0

    pBound = profit # 한계합
    tWeight = weight # temp Weight, 한계합을 계산 시 무게도 고려한다.
    
    j=level+1
    n=len(obj)
    while j<n and tWeight+obj[j][0]<=W: # 배낭안에 넣을 수 있을때까지 더한다.
        tWeight += obj[j][0]
        pBound += obj[j][1]
        j += 1
    
    # 분할 가능한 배낭채우기 문제로 남은 용량을 채운다.
    if j<n : # 배낭의 남은 용량에 대해 처리하기
        pBound += (W - tWeight) * obj[j][1] / obj[j][0] 
    
    return pBound