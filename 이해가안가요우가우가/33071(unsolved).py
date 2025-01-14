import sys
input = sys.stdin.readline

# B-tree를 구성해서 bound를 구성해주면 이분탐색 할 때 편할 거 같다.
# 트리를 이용한 집합과 맵...?

N, K = map(int, input().split())

A = []
A_x = dict()
for i in range(N):
    x, y = map(int, input().split())
    A.append(y)
    if y in A_x: A_x[y].add(x)
    else: A_x[y] = {x}

A.sort()

def binary_search(target, x_set):
    left, right = 0, N-1
    while left <= right:
        mid = (left + right) // 2
        # if len(x_set) == 1 and A_x[A[mid]] == x_set:
        #     if A[mid] < target: left = mid + 1
        #     else: right = mid - 1
        #     continue
        if A[mid] == target:
            return mid
        elif A[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    if len(x_set) == 1 and A_x[mid] == x_set:
        return A[mid]
    else:
        return -1

ans = -1
for i in range(N):
    j = binary_search(K-A[i], A_x[A[i]])
    ans = max(ans, A[i] + j) if (A[i] + j ) <= K else ans
    if ans == K:
        break
print(ans)