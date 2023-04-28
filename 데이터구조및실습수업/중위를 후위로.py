#우선순위: //2 해가지고 리스트 인덱스에 접근해서 몫이 0, 1 이런식으로 출력되서 비교가능하게...
#ex) [+, - , *, /] *, /는 //2(우선순위)가 1이다.
#우선순위가 낮은 녀석이 나오면 펑펑펑펑팝팝팝팝
#스택안에서 (는 넣을때 우선순위가 가장 높지만, 스택안에서는 가장 낮게해야 팝팝팝팝한다.
#괄호닫는거나오면 (나올 때까지 팝팝팝팝하면 비워진다.
#그렇다룽룽링링랑

#식을 입력받는다.
#answer 스택, operator 스택 만들어준다.
#스택에 계속 넣어준다. 오퍼레이터는 따로 넣어준다.
#오퍼레이터는 우선순위에 따라 while문을 써서 파파파파파팝!!!! 해준다.
question = input()

stack = [] #operator will be put in here
answer = []
operator = ['(',')','+','-','*','/'] #operator priority
#you can use dict
#bracket is high priority to push, low priority to pull

def pull():
    while stack:
        temp = stack.pop()
        if temp == '(':
            return
        elif temp == ')':
            continue
        answer.append(temp)
        

for i in question:
    if i in operator:
        if i == '(': #bracket is most high priority so push first
            stack.append(i)
            continue
        elif i == ')':
            pull()
            continue
        elif stack and operator.index(i)//2 == operator.index(stack[-1])//2:
            answer.append(stack.pop())
        elif stack and operator.index(i)//2 <= operator.index(stack[-1])//2: #priority high to low
            pull()
        stack.append(i)
    else:A+B*C
        answer.append(i)
pull()
print(*answer, sep="")