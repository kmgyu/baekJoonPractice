#1018번 체스판 다시칠하기
N, M = map(int, input().split())

question_list = []
oppo_B = 0 #라인마다 두개는 서로 바뀐다. opposite
oppo_W = 1
#타일 일치도
for i in range(N):
    q_temp = input()
    ans_temp = [1] * M
    for j in range(len(q_temp)): #B로 시작하는 모범 타일과 비교한다. 일치도 검사해서 요소합만들어야해서 0으로 만듬.
        if j % 2 == oppo_B:
            if q_temp[j] == 'B':
                ans_temp[j] = 0
        if j % 2 == oppo_W:
            if q_temp[j] == 'W':
                ans_temp[j] = 0

    oppo_W, oppo_B = oppo_B, oppo_W #매 라인마다 모범타일 반전
    question_list.append(ans_temp) #만들어진 ans를 question_list에 삽입
answer_list = []
#N과 M으로 8*8 자르기
cur_x = 0
cur_y = 0
sum_temp = 0
for k in range(N-7):
    for i in range(M-7):
        for j in range(cur_y, cur_y+8): #y축 변화로 먼저 하나 잡은 후에 x를 변경.
            sum_temp += sum(question_list[j][i:i+8])
        answer_list.append(sum_temp)
        sum_temp = 0
    cur_y += 1

answer = min(answer_list)
if 64 - max(answer_list) < min(answer_list):
    answer = 64 - max(answer_list)
print(answer)
