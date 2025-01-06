# ad-hoc 문제. easy 하게 구성할 수 있다. 수학적 패턴을 확인하려면 게임이론이나 그래프 색칠하기 문제를 통해 좀 더 딥-하게 확인할 수 있을 듯
# i * 2 % 5 라는 간단한 수식으로 구성할 수도 있다. 50~65점 짜리 풀이였다. 끄앗
# https://www.acmicpc.net/source/88164127
seq = [1, 4, 3, 2, 5]
seq_idx = [1, 3, 5, 2, 4]

N, M = map(int, input().split())

res = []

res = [[seq[(j+seq_idx[i%5]-1)%5] for j in range(M)] for i in range(N)]

for row in res: print(*row)