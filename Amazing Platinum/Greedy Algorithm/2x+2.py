# https://velog.io/@dombe/baekjoon-19134-python%EC%83%9D%EA%B0%81-%EB%B0%A9%EB%B2%95

def calc(n):
    if n<4:return n
    elif n<10:return ((n+1)//2+1)
    else:return calc((n//2-3)//2)+(n+1)//2+1

print(calc(int(input())))