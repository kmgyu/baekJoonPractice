#10799 쇠막대기
stick = input()
temp = []
count = 0
ans = 0
while len(stick) > 1:
    temp.append(stick[0])
    stick = stick[1:]
    if temp[-1] == stick[0] == "(": #일때
        ans += 1
        count += 1
    elif temp[-1] == stick[0] == ")":
        count -= 1
    else: # ()일때
        if temp[-1] == "(" and count > 0:
            ans += count
print(ans)




#돚거
# bar = list(input())  # 전체 파이프의 개수
# cut = 0  # 잘린 파이프의 개수
# stack = []  # 스택 선언
#
# for i in range(len(bar)):
#     if bar[i] == '(':
#         stack.append('(')  # 스택 쌓기
#
#     else:
#         if bar[i - 1] == '(':  # ()라면 (를 pop(=레이저로 합체)하고 현재 스택에 들어있는 ( 수만큼 답에 값을 더해준다.
#             stack.pop()
#             cut += len(stack)
#
#         else:
#             stack.pop()
#             cut += 1  # 끄트머리 막대기 부분을 더해준다
#
# print(cut)