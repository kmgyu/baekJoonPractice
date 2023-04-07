#1009번 분산처리
for i in range(int(input())):
    a, b = input().split()
    c = int(a[-2:]) ** (int(b)%4+4)
    if c%10 == 0:
        print(10, sep=" ")
    else:
        print(c%10, sep=" ")
print()