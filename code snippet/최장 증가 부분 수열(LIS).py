from bisect import bisect_left

# nlogn 풀이 알고리즘
# 이분 탐색을 이용한다.
# k라는 배열을 이용해 최대한 길이를 길게 만든다.
# 변화된 k의 각 원소는 영향이 없다... 라기 보단 해당 위치에선 영향을 못준다.
# 설명하기 어렵다 으아악
# k자체는 쓸수없고, l_k를 이용해 역추적해서 수열을 구성해야 한다. 이때 DP로 역추적하는 것처럼 여러개 나올 수 있음.
input = open(0).readline

def lis(arr, N):
    k = []
    l_k = []
    for i in range(N):
        idx = bisect_left(k, arr[i])
        if idx == len(k): k.append(arr[i])
        else: k[idx] = arr[i]
        l_k.append(idx+1)
    return l_k