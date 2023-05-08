#회문 검사기
#스페이스나 구두점이면 스택에 삽입하면 안된다. 대소문자도 무시
s = input()
s = s.upper()
extracter = [] #it only take alphabet
for i in s:
    if 65 <= ord(i) < 91:
        extracter.append(i)
stack = []
n=len(extracter)//2 # 문자열... 갈랐다고....
for i in range(n):
    stack.append(extracter.pop())
if len(extracter) > len(stack): # 길면 가운데 하나 빼준다.
    extracter.pop()
for i in range(n):
    if extracter.pop() != stack.pop():
        print("NO") #응 아니야.
        exit()
print("yes~~~~~") #네 맞워용~~~~~~

