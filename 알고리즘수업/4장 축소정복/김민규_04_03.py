def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"pass [{i}] : {arr}")
    return arr

# arr = [7,4,9,6,3,8,7,5]

# print(insert_sort(arr))

