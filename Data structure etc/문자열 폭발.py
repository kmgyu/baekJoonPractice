li = list(input()) #입력받은 문자열
bomb = list(input()) #폭발 문자열
k = len(bomb)
ans = []
for i in range(len(li)):
    ans.append(li[i]) #pop(n)을 할 경우 시간복잡도는 n이 된다. 입력안하면 1임. 주의하자. 이거땜에 틀렸다 ㅅㅂ...
    if ans[-k:] == bomb:
        for i in range(len(bomb)):
            ans.pop()
if ans:
    print(*ans, sep="")
else:
    print("FRULA")
#시간 복잡도가 O(N)인 스택을 만들자.
#