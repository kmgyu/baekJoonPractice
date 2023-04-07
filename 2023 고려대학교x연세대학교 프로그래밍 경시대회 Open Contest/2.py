n = int(input()) #length
num = list(map(int, input().split()))
num.sort()
single = []
double = []
for i in range(1, n):
    for j in range(i, n):
        if (num[j]-num[i-1]) % 2 == 0:
            double.append(num[j]-num[i-1])
        else:
            single.append(num[j]-num[i-1])
if double:
    print(min(double), end=" ")
else:
    print(-1, end=" ")
if single:
    print(min(single))
else:
    print(-1)