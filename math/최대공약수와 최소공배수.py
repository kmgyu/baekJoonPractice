# 2609번 최대공약수와 최소공배수
# 유클리드 호제법의 원리는 나머지로 몫을 나누어
# 나누어 떨어지는 수가 나올때까지 나누는 것.
# 안나오면 1이 되는거고. 나누어 떨어지는 수가 이때 최소공약수가 된다.
a, b = map(int, input().split())
num = a*b
# if a < b : 정렬은 없어도 무관.
#     a, b = b, a
while b > 0:
    temp = a
    a = b
    b = temp%b
print(a)
print(num//a)