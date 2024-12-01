# selection sort

def selection_sort(l):
    n = len(l)
    for i in range(n):
        minor = i
        for j in range(i, n):
            if l[i] > l[j]:
                minor = j
        l[i], l[minor] = l[minor], l[i]
    return l

# test driver
arr = [3, 2, 1, 4, 5]

print(selection_sort(arr))