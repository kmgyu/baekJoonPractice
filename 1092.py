from heapq import heappush, heappop

input = open(0).readline

N = int(input())
crain = sorted(map(int, input().split()))

M = int(input())
boxes = sorted(map(int, input().split()))

current = N-1
q = []
# 현재 부하가 적은 크레인부터 가중
for i in range(M-1, -1, -1):
    while current >= 0:
        # 현재 무게에 맞는 크레인 끌어 오기.
        # 역순으로 루프를 진행하기 때문에 이 이후에 오는 모든 박스를 들 수 있음.
        # 따라서 크레인의 무게 제한은 이용할 필요가 없음.
        if crain[current] >= boxes[i]:
            heappush(q, 0)
            current -= 1
        else: break
    if q: heappush(q, heappop(q)+1) # 가장 부하가 적은 크레인을 이용해 가중
    else: break # 못 든다. => 정렬되어 있음. 이후도 똑같은 결과. 시간 절약을 위해 종료.

print(max(q) if q else -1)
