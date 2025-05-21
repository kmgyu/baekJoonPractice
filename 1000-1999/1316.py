cnt = 0
for i in range(int(input())):
    s = input()
    check = set()
    temp = s[0]
    for i in s:
        if temp != i and i in check:
            cnt -= 1
            break
        if i != check:
            check.add(i)
        temp = i
    cnt += 1
print(cnt)