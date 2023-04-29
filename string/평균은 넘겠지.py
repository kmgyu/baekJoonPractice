for i in range(int(input())):
    stu = list(map(int,input().split()))
    aver = sum(stu[1:])/stu[0]
    cnt = 0
    for i in range(1, stu[0]+1):
        if stu[i] > aver:
            cnt+=1
    print(f"{(cnt/stu[0]) * 100:.3f}%")