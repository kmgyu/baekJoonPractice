cat = 0
cnt = 0
def create():
    global cat, cnt
    cat += 1
    cnt += 1
def copy():
    global cat, cnt
    if n - cat > cat:
        cat += cat
    else:
        cat += n-cat
    cnt += 1
    #k마리일때
    #0마리 이상 k마리 이하 고양이를 집에 추가가능

#최소 행동횟수 출력하기

n = int(input())
if n > 0:
    create()
while n > cat:
    copy()
print(cnt)