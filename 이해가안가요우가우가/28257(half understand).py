#unsolved
# https://wondev.tistory.com/173
# 으아ㅏㅏㅏ아ㅏㄱ 왤케 왤케임

def Solve(N):
    if N == 1:
        return 1
    
    section = 0
    
    left, right = 0, 10**9
    
    n = N
    
    # 이분 탐색을 통한 적절한 민트초코 총합 찾기
    # 이를 통해 섹션의 위치 추정
    while left <= right:
        mid = (left + right)//2
        mint = mid * (3 * mid - 1) //2 # 민트초코 총합 공식
        
        if mint >= N:
            section = mid
            right = mid - 1
        else:
            left = mid + 1

    prev_section = section - 1
    n -= prev_section * (3 * prev_section - 1) // 2 # 현재 섹션 기준으로 몇번째 민트인지 계산
    
    line = 2 + (section - 2) * 3 # 첫번째 섹션은 1, 0이라 제외하고 나중에 추가. 현재 라인 구하기
    total = (1 + line) * line // 2 # 현재 초콜릿 위치(갯수)
    
    # section의 패턴
    # 초코 갯수는 line + 1, line + 2, line + 1 패턴이다.
    # 거기에다... 값들 계산해서 넣어주는데 계산식 개빡세서 잘 이해안ㄷ으애래ㅐㄱ
    # 브루트 포스 쓰면 머리는 편해지지만 시간초과 걸리낟. 구아악
    
    if n <= section - 1 :
        total = total + 2 + (n-1) * 3
    elif n <= section * 2 - 1:
        total = total + (line + 1) + 1 + (n - (section - 1) - 1) * 3
    else:
        total = total + (line + 1) + (line + 2) + 3 + (n - (section * 2 - 1) - 1) * 3
    return total
    
    
T = int(input())
for _ in range(T):
    ans = Solve(int(input()))
    print(ans)