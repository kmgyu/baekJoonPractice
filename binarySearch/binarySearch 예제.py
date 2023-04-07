def binary_search(array, target, start, end):
    if start> end:
        return None
    mid = (start+end) //2
    # 왜 start가 end보다 커질까...

    #값 찾았다.
    if array[mid] == target:
        return mid
    # 원하는 값이 중간점보다 작을 때
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    #원하는 값이 중간점보다 클 때
    else:
        return binary_search(array, target, mid+1, end)