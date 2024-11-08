def quick_sort(A, left, right):
    if left<right:
        pivot = partition(A, left, right)
        quick_sort(A, left, pivot-1)
        quick_sort(A, pivot+1, right)

def partition(A, left, right):
    # Hoare Partition
    low = left+1
    high = right
    pivot = A[left]
    print(f'인덱스 {left} 기준 호어 분할 시작 : {A}')
    while (low <= high):
        while low <= right and A[low] <= pivot: low += 1
        while high >= left and A[high] > pivot: high -= 1
        
        if low < high:
            A[low], A[high] = A[high], A[low]
            print(f'{A[low]}와 {A[high]} 교환 : {A}')
    
    A[left], A[high] = A[high], A[left]
    print(f'인덱스 {high} 기준 호어 분할 결과 : {A}')
    return high

input2 = [71, 49, 92, 55, 38, 82, 72, 53]

if __name__ == "__main__":
    quick_sort(input2, 0, len(input2)-1)
    print(input2)