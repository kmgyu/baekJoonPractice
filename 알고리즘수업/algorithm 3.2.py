# sequential search

def sequantial_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = [3, 2, 1, 4, 5]
key = 3
print(sequantial_search(arr, key))