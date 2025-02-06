# https://yabmoons.tistory.com/592
# https://velog.io/@sunkyuj/python-%EB%B0%B1%EC%A4%80
# A to B 가 팰린드롬일 때에 대한 증명... 이것 또한 dp이다.
# 축소문제와의 연관성을 메모이제이션

S = input()
l = len(S)
dp = [[False] * l for _ in range(l)]