N, M = map(int, input().split())
nums = []
for i in range(M):
    a, b = map(int, input().split())
    nums.append((a, min(b, N)))

dp = [[0] * (N+1) for _ in range(M+1)]

# 흠....
# 그리디 + dp?
# 1. 수가 큰것부터 정렬해서 N을 차곡차곡 기록해준다.
# 2. 정석적인 배낭문제처럼 구성하는데, i가 j의 배수라면 기록한다...? i+1 패턴이 아니라 i랑 j의 2중 for문?
# 3. 해가 완성되면 곧바로 종료한다. 왜냐 정렬한 후 내림차순 정렬된것은 이미 완성된 것으로 볼 수 있기 때문에...?
# 사실 직감이다. 나도 잘 몰라 웅앵앵