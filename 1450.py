from bisect import bisect_right

# https://velog.io/@dark6ro/%EB%B0%B1%EC%A4%80-1450%EB%B2%88-%EB%83%85%EC%83%89%EB%AC%B8%EC%A0%9C
# https://banwolcode.tistory.com/51
# Meet in the middle(중간에서 만나기)를 이용하는 문제

# 주소포인팅을 이용하긴 했는데... 헷갈릴지도 모르겠다.
# combination 말고 이런식으로도 만들 수 있다!
def dfs(lst, sum, target, end_p):
    if target != end_p:
        lst.append(sum + weights[target])
        dfs(lst, sum + weights[target], target + 1, end_p)
        dfs(lst, sum, target + 1, end_p)

def solve():
    cnt = 0
    for i in weights1:
        cnt += bisect_right(weights2, C-i)
    return cnt

N, C = map(int, input().split())
weights = list(map(int, input().split()))

# 아무것도 안넣은 경우도 고려해야 한다.
# 이렇게 설정할 경우, weights1에서 weights2 대상 이분 탐색 시 0이면 찾을게 없다는 것이 된다.
# 딱코일 때는... 모르겠다. index = 0일 텐데...?
# 응 그래서 실제로 카운트 안한다.
weights1, weights2 = [0], [0] 
dfs(weights1, 0, 0, N//2)
dfs(weights2, 0, N//2, N)

# 이분탐색 할거니까 정렬
weights1.sort()
weights2.sort()

print(solve())