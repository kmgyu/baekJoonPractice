#우선순위: //2 해가지고 리스트 인덱스에 접근해서 몫이 0, 1 이런식으로 출력되서 비교가능하게...
#ex) [+, - , *, /] *, /는 //2(우선순위)가 1이다.
#스택안에서 (는 넣을때 우선순위가 가장 높지만, 스택안에서는 가장 낮게해야 팝팝팝팝한다.
#괄호닫는거나오면 (나올 때까지 팝팝팝팝하면 비워진다.
#그렇다룽룽링링랑

#식을 입력받는다.
#answer 스택, operator 스택 만들어준다.
#스택에 계속 넣어준다. 오퍼레이터는 따로 넣어준다.
#오퍼레이터는 우선순위에 따라 while문을 써서 파파파파파팝!!!! 해준다.
question = list(input().split())

stack = [] #operator will be put in here
answer = []
operator = ['(',')','+','-','*','/'] #operator priority
#딕셔너리로 우선순위 키값 넣을수도 있음.
#괄호는 넣을 때 우선순위가 제일 높고, 나올때 제일 낮다.
for i in question:
    if i in operator:
        if operator.index(i)//2 < stack[-1]: #우선순위 비교
            pass
        stack.append(i)
        
    else:
        answer.append(int(i))