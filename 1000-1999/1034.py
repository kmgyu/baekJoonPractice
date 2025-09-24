
n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(input())
    
k = int(input())

cnt = 0
for col in range(n):
    # 0 개수
    z_cnt = 0
    for num in lst[col]:
        if num == '0': z_cnt += 1
    # 이 행과 똑같은 값을 가진 행의 개수 세기
    col_same = 0
    if z_cnt <= k and z_cnt%2 == k%2:  # 0의 개수 <= 기회이며 홀짝성이 같아야 1로 만들 수 있음.
        for col2 in range(n):  # 가능성 확인했으므로 나이브하게 전위 순회 및 같은 정보를 가진 행에 대해 카운팅
            if lst[col] == lst[col2]: col_same += 1
    cnt = max(cnt, col_same)
print(cnt)