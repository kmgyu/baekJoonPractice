#회문 검사기
#스택을 이용한 회문 검사 팰린드롬등등 알랄랄랄랄랄 뽈롱ㄹ뽈롱~
#스페이스나 구두점이면 스택에 삽입하면 안된다. 대소문자도 무시
s = input()
s = s.upper()
extracter = [] #it only take alphabet
for i in s:
    if 65 <= ord(i) < 91:
        extracter.append(i)
stack = []
n=len(extracter)//2
for i in range(n):
    stack.append(extracter.pop())
if len(extracter) > len(stack):
    extracter.pop()
for i in range(n):
    if extracter.pop() != stack.pop():
        print("NO")
        exit()
print("yes~~~~~")

