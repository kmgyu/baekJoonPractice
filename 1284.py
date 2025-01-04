from sys import stdin
input = stdin.readline
while True:
    n = input().rstrip()
    if n == '0':
        break
    ans = 1
    for i in n:
        if i == '0':
            ans += 4
        elif i == '1':
            ans += 2
        else:
            ans += 3
        ans+=1
    print(ans)