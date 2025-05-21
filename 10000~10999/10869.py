# 사칙연산 +-*몫나머지 출력하는 프로그램을 만들어라.

data = input().split()
data = list(map(int, data))
print(data[0]+data[1])
print(data[0]-data[1])
print(data[0]*data[1])
print(data[0]//data[1])
print(data[0]%data[1])