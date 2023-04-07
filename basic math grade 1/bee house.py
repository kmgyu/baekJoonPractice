#2292번
room = int(input())
count = 1
move = 1
while room > move:
    move += count*6
    count += 1
print(count)
"""
이 문제를 푸는 법은 배열로 직접 구현해서 최단거리를 이동하는 그런어려운 문제가 아니다!
1을 둘러싼 6가지 숫자, 그 다음 그 6개를 둘러싼 12가지 숫자.... 이런 식으로 계차수열로 늘어나는 것을 이용하는 문제이기 때문에 그런식으로 접근할 필요가 없다. 우리는 최단거리만 필요하기 때문에!!!!
"""

"""
https://www.acmicpc.net/board/view/99363
import sys

n = int(sys.stdin.readline())
x = ((n-1)/3)**(1/2)
print(round(x)+1)
계차수열을 이용한 최적화된 식이다 링크는 위의 코드에 대한 설명.
"""