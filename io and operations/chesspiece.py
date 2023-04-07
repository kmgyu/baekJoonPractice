#체스말 킹,퀸,비숍,나이트,룩,폰 순으로 있다. 부족한 부분이나 많은 부분 출력하는 코드작성

piece = list(map(int, input().split()))
standard = list(map(int, [1, 1, 2, 2, 2, 8]))
for x in range(0, 6):
    piece[x] = standard[x] - piece[x]
result = list(map(str, piece))
print(" ".join(result))