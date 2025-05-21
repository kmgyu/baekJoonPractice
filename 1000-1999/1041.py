#1041번
n = int(input()) #주사위의 크기
num = list(map(int, input().split())) 
case2_li = []
case3_li = []
for i in range(6):
    for j in range(6):
        if i != j and (i,j) != (0,5) and (i,j) != (5,0) and (i,j) != (1,4) and (i,j) != (4,1) and (i,j) != (2,3) and (i,j) != (3,2):
            case2_li.append(num[i]+num[j])
case3_li = [num[0]+num[1]+num[2], #123
            num[0]+num[1]+num[3], #124
            num[0]+num[3]+num[4], #145
            num[0]+num[2]+num[4], #135
            num[5]+num[1]+num[2],
            num[5]+num[1]+num[3],
            num[5]+num[3]+num[4],
            num[5]+num[2]+num[4]]
case1 = min(num) # 가운데면
case2 = min(case2_li) #모서리. 아래 4개에 + 모서리
case3 = min(case3_li) #3면이 보이는 경우. 4개만 있음.

ans = 0
if n == 1:
    ans = sum(num) - max(num)
else:
    ans += case3 * 4
    ans += case2 * ((n-1)*4 + (n-2)*4)
    ans += case1 * ((n-2)**2 + (n-1) * (n-2) * 4)
print(ans)