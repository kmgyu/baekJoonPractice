N = int(input())
A = [*map(int, input().split())]
S = int(input())

# S가 1_000_000 넘는다. n <= 50이다. 멈추기용
perfect = sorted(A, reverse=True)

# 특수한 삽입정렬 규칙이다.
def insert(idx):
    global S, A
    target = A[idx]
    
    change = A[idx+1]
    change_idx = idx+1
    for i in range(idx+2, N):
        # 현재 인덱스 기준 S 충분하지 않으면 탈출
        if S < i-idx: break
        
        if A[i] > change:
            change_idx = i
            change = A[i]
    
    # print(idx, change, change_idx)
    if target < A[change_idx]:
        S -= change_idx-idx
        l,r = idx,change_idx
        A = A[:l] + [A[r]] + A[l:r] + A[r+1:]

while S > 0:
    if A == perfect: break
    
    for i in range(N-1):
        insert(i)
        if S <= 0: break

print(*A)