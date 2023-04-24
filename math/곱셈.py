# https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B0%B1%EC%A4%80-1629%EB%B2%88-%EA%B3%B1%EC%85%88-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython
a, b, c = map(int, input().split())
def dac(a, b):
    if b == 1:
        return a%c
    temp = dac(a, b // 2)
    
    if b % 2 == 0:
        return temp*temp%c
    else:
        return temp*temp*a%c
print(dac(a,b))