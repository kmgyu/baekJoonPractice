#예제이다. 입력만 받을 거면 리스트안의 내용만 지우면 된다.
task = [['지역봉사회',9,13],
        ['바둑회',11,14],
        ['문학회',13,16],
        ['독서회',14,15],
        ['토론회',10.5,11.5],
        ['서예회',9,11],
        ['사진회',15,17]
        ]

#입력을 받을 경우
#얼마나 입력받을지 알 수 없으므로 while을 썼다.
#아무것도 입력하지 않으면 입력을 중지하고 코드가 진행된다.
temp = []
while True:
    temp = list(input().split())
    if len(temp) == 0:
        break
    temp[1],temp[2] = map(int, (temp[1], temp[2]))
    task.append(temp)
    

#시작시간과 종료시간이 같은 경우가 있다.
#이때, 정렬이 제대로 되지않으면 반례가생길수있기때문에
#시작시간순으로 정렬후, 종료시간순으로 정렬을 해준다.
task.sort(key=lambda x:x[1])
#종료시간 순 정렬
task.sort(key=lambda x:x[2])

count = 0
time = 0
for i in task:
    if time == 0 or i[1] >= time:
        #처음 수행하거나, 시작시간이 종료시간보다 뒤일때.
        time = i[2]
        count += 1
#가장 긴 길이가 나온다.
print(count)