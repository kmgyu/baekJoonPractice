# 돚거 https://velog.io/@waoderboy/BOJ-%EB%B0%B1%EC%A4%80-2138-%EC%A0%84%EA%B5%AC%EC%99%80-%EC%8A%A4%EC%9C%84%EC%B9%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC

n = int(input())
bulb = list(map(int, input()))
target = list(map(int, input()))

def change(A, B):
    A_copy = A[:]
    press = 0
    for i in range(1, n):
        
        if A_copy[i-1] == B[i-1]:
            continue
        
        press += 1
        for j in range(i-1, i+2):
            if j<n:
                A_copy[j] = 1 - A_copy[j]
    if A_copy == B:
        return press 
    else:
        return 1e9

res = change(bulb, target)
# 첫번째 전구의 스위치를 누르는 경우
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
#비교
res = min(res, change(bulb, target) + 1)# min(첫번째 전구x, 첫번째 전구 o)
if res != 1e9:
    print(res)
else:
    print(-1)