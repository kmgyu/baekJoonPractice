# TED의 로직을 참고하였다...
# https://zenith-feature-prismic.staging.ted.com/talks/jennifer_lu_can_you_solve_the_counterfeit_coin_riddle?subtitle=en


def coin_compare(coins):
    # 각 그룹 별로 분할
    # 코드 편의상 리턴 이전에 코인의 무게를 구하고, index()를 사용해 리턴...
    group1 = coins[0:4]
    group2 = coins[4:8]
    group3 = coins[8:12]
    
    gr1_sum = sum(group1)
    gr2_sum = sum(group2)
    
    coin_weight = 0
    if gr1_sum == gr2_sum:
        print('case 1', end=' ')
        coin_weight = case_1(group1, group3)
    else:
        print('case 2', end=' ')
        coin_weight = case_2(group1, group2, group3, 1 if gr1_sum > gr2_sum else -1)
    return coin_weight, coins.index(coin_weight)

def case_1(group1, group3):
    # group1, group2의 무게가 같은 경우
    # group1 : 정상, group3 : 위조 의심
    gr1_sum = sum(group1[:3]) # 3개만 가져옴
    gr3_sum = sum(group3[:3]) # 마찬가지로 3개만
    if gr1_sum == gr3_sum:
        # 두 동전그룹이 같으면 남은 동전이 위조동전
        return group3[-1]
    else:
        return tri_compare(group3[:3], 1 if gr1_sum < gr3_sum else -1)

def case_2(group1, group2, group3, state):
    # group1을 무게 비교의 기준으로 삼는다. (위조 의심군)
    # group1, group2의 무게가 다른 경우. group3은 정상 동전 그룹
    # state : group1이 무거우면 1, 가벼우면 -1
    group_A = [*group1[:3], group2[-1]]
    group_B = [*group3[:3], group1[-1]]
    
    grA_sum = sum(group_A)
    grB_sum = sum(group_B)
    
    if grA_sum == grB_sum:
        print('grA == grB', end=' ')
        # group2의 나머지가 위조 동전.
        # group1은 group1의 상태의 반대이다.
        return tri_compare(group2[:3], state*-1)
    else:
        # group A가 무거운 케이스
        # group1이 무거웠을 경우 group1, groupA에 모두 사용된 것이 위조 동전
        # group1이 가벼웠을 경우 case a로 넘어감
        # group A가 가벼운 케이스
        # group1이 무거웠을 경우 case a로 넘어감
        # group1이 가벼웠을 경우 group1, groupA에 모두 사용된 것이 위조 동전
        # 따라서 XNOR 연산으로 if 문 압축
        case_state = 1 if not (grA_sum > grB_sum)^(state == 1) else -1
        # case a: group2[-1]과 group[-1]의 동전이 위조 동전으로 의심되는 경우
        # tri_compare()는 0과 1을 비교하기 때문에 반드시 1번 혹은 0번에 정상 그룹의 동전을 넣어주어야 함.
        case_a_coin = [group1[-1], group3[0], group2[-1]]
        if case_state == 1:
            print('group a is liar')
            return tri_compare(group1[:3], state)
        else:
            print('case_a need to compare')
            return tri_compare(case_a_coin, state)


def tri_compare(coins, state):
    # 3개의 동전을 비교시.
    # state 1 : 무거움, -1 : 가벼움
    if coins[0] == coins[1]:
        return coins[2]
    # coins[0] > coins[1], state == 1를 XNOR 연산함. (이중 if문 압축)
    return coins[0] if not (coins[0] > coins[1])^(state == 1) else coins[1]
    
def test(fake_weight):
    coincoin = [[1]*12 for _ in range(12)]
    for i in range(12):
        coincoin[i][i] = fake_weight

    for coin in coincoin:
        coin_info = coin_compare(coin) # weight, index
        print(f'answer ::: coin weight was {coin_info[0]} and index is {coin_info[1]}')
    
# test driver
print("test case 1, fake coin is light weight")
test(-1)

print("test case 2, fake coin is heavy weight")
test(2)
