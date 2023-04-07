n = int(input())
alphabet = []  # 변수 저장
stack = [] #좌표값을 저장한걸 값으로 변환
num = input() #입력 받은 값.
for i in range(len(num)):
    if len(alphabet) <= ord(num[i]) - 65 : #새로운 변수가 추가
        alphabet.append(int(input()))
    if num[i] == "+":
        stack[-2] += stack[-1]
        stack.pop()
        continue
    elif num[i] == "-":
        stack[-2] -= stack[-1]
        stack.pop()
        continue
    elif num[i] == "*":
        stack[-2] *= stack[-1]
        stack.pop()
        continue
    elif num[i] == "/":
        stack[-2] /= stack[-1]
        stack.pop()
        continue
    stack.append(alphabet[ord(num[i])-65]) #좌표값 저장
print("{0:0.2f}".format(stack[0]))
