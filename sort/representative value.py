num = [int(input()) for i in range(5)]
print(int(sum(num)/len(num)))

for i in range(5):
    min = i
    for j in range(i, 5):
        if num[j] < num[min]:
            min = j
    num[min], num[i] = num[i], num[min]
print(num[2])

