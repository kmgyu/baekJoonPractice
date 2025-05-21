# 이분 탐색보다는 매개변수 탐색에 가까운 문제...?
# 머리를 열심히 굴릴 것.
X, Y=map(int,input().split()) 
Z =(100*Y)//X 
left = 0 
right = X
answer = 0
if Z >= 99: answer = -1
else: 
    while left <= right: 
        mid = (left+right)//2 
        if (100*(Y+mid))//(X+mid)>Z:
            answer = mid 
            right = mid - 1 
        else: 
            left = mid + 1
print(answer)