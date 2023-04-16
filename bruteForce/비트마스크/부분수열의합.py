n, s = map(int, input().split())
arr = [i for i in list(map(int,input().split()))]
cnt = 0

def func(cur, tot):
    #cur은 현재 몇번 원소까지 선택한지 카운트, tot은 현재까지의 합.
    #모든 원소에 대해 합할지 안할지 선택한 한 가지의 경우의 수를 구할 때 당연히 cur횟수가 원소의 수와 같아진다.
    global cnt
    if cur == n:
        if tot == s: cnt += 1
        return
    func(cur+1, tot) #현재 원소를 합하지 않는 경우
    func(cur+1, tot+arr[cur]) #현재 원소 합하는 경우

func(0,0)
if s == 0: cnt -= 1 #s가 0일때 공집합도 카운트되므로 하나 빼야된다.
print(cnt)