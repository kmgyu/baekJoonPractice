N, k = map(int, input().split())
num = list(map(int, input().split()))

for i in range(len(num)):
    min = i
    for j in range(i, len(num)):
        if num[j] < num[min]:
            min = j
    num[min], num[i] = num[i], num[min]

print(num[-k])




