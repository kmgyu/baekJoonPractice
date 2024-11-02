def quick_select(A, left, right, k):
    pos = partition(A, left, right)
    
    if (pos+1 == left + k):
        return A[pos]
    elif (pos+1 > left+k):
        print(f'인덱스 {pos} 기준 왼쪽 탐색')
        return quick_select(A, left, pos-1, k)
    else:
        print(f'인덱스 {pos} 기준 오른쪽 탐색')
        return quick_select(A, pos+1, right, k-(pos+1-left))

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

# test driver
A = [12, 5, 7, 9, 18, 3, 8] # target array
k = len(A)//2+1 # 중앙값 인덱스 A의 길이가 홀수이므로 가능하다…!

median = quick_select(A, 0, len(A)-1, k) # 중앙값
print(median)