# back tracking + branch & bound let's go
# https://www.acmicpc.net/board/view/152894
# referenced
import copy

def rotate_90(m):
    # 90도 회전 함수(반시계 방향)
    # 크아아아앗 개쩔잔아
    M = len(m)
    tmp = [[0] * M for _ in range(M)]

    for r in range(M):
        for c in range(M):
            tmp[c][M-1-r] = m[r][c]
    return tmp


def push(board):
    # 방향만 돌리고 미는 건 똑같은 함수로 한다.
    # 이런 식으로 생각해야 한다....

    # 임시 보드
    tmp_board = []
    for row in board:
        stack = []
        tmp = 0
        # tmp에 임시 값을 저장한다. (합치기 용)
        # 만약 value 조회 시 0일경우? 공실이니 skip.
        # value가 tmp와 같으면 합치고 stack(병합되는 행)에 추가. tmp는 초기화한다.
        # value와 tmp가 다르면, tmp가 0이 아닐 경우만 추가하고 tmp를 갱신한다.
        for value in row:
            if value == 0: continue
            if value == tmp:
                stack.append(tmp * 2)
                tmp = 0
            else:
                if tmp > 0: stack.append(tmp)
                tmp = value
        # tmp가 0 이상일 경우. 이때는 합쳐지지 않는 경우다. 그래서 추가해줌.
        if tmp: stack.append(tmp)
        # zero fill
        for _ in range(len(stack), N): stack.append(0)
        
        tmp_board.append(stack)
    return tmp_board


def recur(idx, board):
    if idx == 5:
        cur_max = 0
        for i in range(N):
            cur_max = max(cur_max, *board[i])
        return cur_max
    
    new_board = copy.deepcopy(board)
    board_90 = rotate_90(board)
    board_180 = rotate_90(board_90)
    board_270 = rotate_90(board_180)

    return max(
        recur(idx + 1, push(new_board)),
        recur(idx + 1, push(board_90)),
        recur(idx + 1, push(board_180)),
        recur(idx + 1, push(board_270))
        )

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

print(recur(0, arr))
