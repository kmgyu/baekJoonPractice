#8958

for _ in range(int(input())):
    q_list = input()
    count = 0
    ans = 0
    for i in q_list:
        if i =="O":
            count += 1
            ans += count
        else:
            count = 0
    print(ans)