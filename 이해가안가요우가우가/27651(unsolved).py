input = open(0).readline

N = int(input())
A = [*map(int, input().split())]

sums = [0] # 누적 합
for i in range(N): sums.append(A[i] + sums[-1])

def get_middle(l, r):
    if l > r: return 0
    return sums[r+1] - sums[l]

answer = 0

left, right = 1, N-2
for i in range(N-2):
    
    head = get_middle(0, i)
    
    left = max(left, i+1)
    while right > 0 and get_middle(right+1, N-1) <= head: right -=1
    while left < right and \
        get_middle(i+1, left) <= get_middle(left+1, N-1):
            left += 1
    # print(i, left, right)
    # print(head, get_middle(i, left), get_middle(left, N-1))
    answer += max(0, right - left + 1)
print(answer)