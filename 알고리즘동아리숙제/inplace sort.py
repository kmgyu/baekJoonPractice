import random
unsorted = [random.randrange(1,100) for _ in range(20)]
sorter = sorted(unsorted)
size = len(unsorted)
for i in range(1, size):
    for j in range(i):
        if unsorted[j] > unsorted[i]:
            unsorted.insert(j, unsorted.pop(i))
        # print(*unsorted, sep=", ")

print(unsorted == sorter)
#삽입정렬
#inplace sort는 메모리를 그렇게 많이 소모하지 않는 정렬들을 말함.