# modular 동치를 이용한 방법
# 유클리드 호제법에서의 아이디어처럼, 숫자를 너무 커지지 않게 하기 위해 N으로 나누어준다.
# N아 0이 되면 정답...
# N이 2나 5의 배수면 못만드니까 false...
# 골드 5던데 이것도 바로 못푸는거면 뇌가 썩어버린건가

n = int(input())
r = 1
cnt = 1

if n % 2 == 0 or n % 5 == 0:
    print(-1)
else:
    while True:
        if r%n == 0:
            print(cnt)
            break
        r = (r * 10 + 1) % n
        cnt += 1