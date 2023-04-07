# 만들어주는 함수
# count 계산해서 0될때까지 함수호출
#
# 매개변수
# 인풋 리스트, 카운트
#
# 하는거
# 카운트 -= 1
# 인풋 리스트를 받아서 템포러리 공백파일 생성(spacebar) 인풋 리스트 3번반복, 1 0 1, 3번반복 answer 리스트생성
#
# 어떻게 붙여야 할까?
# 리스트를 계속늘리면 안될지도 몰라... extend로 그냥 2차원 배열을 늘려야한다...
# 구조가 복잡해지기 때문에 2차원 배열을 게속해서 붙이자
#
# 3일때, 1 *을 만든다.
# 9이상일 때, n/3 * " "을 가운데에 추가한다.
# 이 크기를 어떻게 추가하지? 범위가 n/3 * n/3이다. 나머지는 받은 리스트를 복제하면 된다.
# 야호! 이거 완전 쉬워요~

n = int(input())
ex = ["***", "* *", "***"]
def star(n) :
    if n == 3:
        return ex
    else:
        li = [arr * 3 for arr in star(n//3)] + [arr + " "*(n//3) + arr for arr in star(n//3)] + [arr*3 for arr in star(n//3)]
        #문자열을 리스트 컴프리헨션으로 *3 하고 계속 더해주고, star 재귀 호출
        return li
for arr in star(n):
    print(arr) #문자열 출력

# 내가 만든 비효율적인 답
# while n > 3:
#     temp = []
#     for i in range(3):
#         for j in range(len(ans)):
#             temp.append(ans[j][0:])  # 세로 1열 추가 #주소값을 더해준 것으로... 추정! 따라서 리스트 슬라이싱!
#     cur = 0
#
#     for i in range(len(ans) * 3):
#         if len(ans) <= i < len(ans) * 2:
#             temp[i].extend([len(ans) * " "] + ans[cur])
#         else:
#             temp[i].extend(ans[cur] * 2)
#         cur += 1
#         if cur > len(ans)-1:
#             cur = 0
#     ans = temp
#     n = n/3