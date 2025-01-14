#24313
a1, a0 = map(int, input().split())
a1 = a1 - int(input())
n = int(input())
temp = 1
while a1*n + a0 >= 0:
    if a1*n + a0 > 0:
        temp = 0
        break
    n += 1
if a1 > 0:
    temp = 0
print(temp)