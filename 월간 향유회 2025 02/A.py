n = int(input())
s = input()
cnt = 0
border = 1
for i in range(1, n):
    if s[i] == '1':
        cnt += border
        border = 0
    elif s[i] == '0':
        border += 1

print(cnt)