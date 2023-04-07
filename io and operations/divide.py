# A B 형식으로 입력 후 나눠라. 10^-9승까지 근사치여야 한다. 굳이 출력할 필요는 없음.

data = input("input data: ").split()
data = list(map(int, data))
result = data[0]/data[1]
print("%0.9f" % result)