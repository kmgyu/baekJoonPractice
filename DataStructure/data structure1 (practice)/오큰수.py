#17298번 오큰수
n = int(input()) #순열 크기
A = list(map(int, input().split())) #순열 A
stack = []
ans = []
cur = 0

for i in range(n):
    while len(stack) != 0 and stack[-1] <= A[-1]: #스택이 0이 되거나 앞에 있는 것보다 작은 수는 다 쳐낼때까지 pop
        stack.pop()
    if len(stack) == 0: #길이 없으면 -1을 답변에 넣는다.
        ans.append(-1)
    else:
        ans.append(stack[-1]) #가장 가까운 큰 값을 넣어준다.
    stack.append(A.pop()) #마지막에 게속해서 스택에 A순열의 값을 넣어준다.

ans = list(reversed(ans))
print(*ans)

# N = int(input())
# A = list(map(int, input().split()))
# stack = []
# ans = [-1]*N
# front = 0
# for i in range(N):
#     while stack and A[stack[-1]] < A[i]: #stack이 인덱스 위치를 저장하는 역할이다. stack 위치의 A가 더 크면 스킵하고 인덱스 위치는 저장. i의 위치가 더크면 팝팝팝
#         ans[stack.pop()] = A[i]
#     stack += [i]
# print(*ans)