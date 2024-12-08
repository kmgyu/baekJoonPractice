def knapsack_greedy(obj, W):
    # obj : (물건 이름, 무게, 가치)의 튜플 리스트
    obj.sort(key = lambda x: x[2]/x[1], reverse = True)
    
    totalValue = 0 # 배낭에 들어간 물건들의 가치
    for o in obj:
        if W <= 0: break # 용량이 다 찬 경우
        if W - o[1] >= 0: # 물건 전체가 들어갈 수 있는 경우
            W -= o[1]
            totalValue += o[2]
        else: # 물건의 일부만 넣을 수 있는 경우
            fraction = W/o[1]
            totalValue += o[2]*fraction
            W = int(W - o[1]*fraction) # 소수점 삭제
    
    return totalValue