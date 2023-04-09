#1712번 문제
from math import *
a, b, c = map(int, input().split())
profit = c - b
try:
    even_point = ceil((a / profit))  # 손익분기점
except:
    even_point = 0
if profit <= 0:
    print(-1)
elif a % profit == 0:
    print(even_point+1)
else :
    print(even_point)

#소수점으로 나뉘는 경우, 정수로 나뉘는 경우를 구분하도록 하자!

#ceil : 올림 / floor : 내림 / round : 반올림
#고정비용 a가 이익인 even_point보다 큰 경우가 있기 때문에 무조건 올림인 ceil을 쓰는게 맞다...! 주의해서 사용하자.
#c - b = 0 이되면 zeroDivisionError가 생긴다. 하지만 try except를 이용해 이렇게 간단하게 피했습니다 인정합니다 인정빔 발싸 푸쓔우우웅
"""
더 간단한 방식

a,b,c = map(int,input().split())

if b>=c:
    print(-1)
else:
    print(a//(c-b)+1)
"""