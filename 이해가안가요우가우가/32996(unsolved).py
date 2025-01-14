N = int(input())

# example = [[1, 2, 3, 4],
#            [2, 3, 4, 1],
#            [3, 4, 1, 2],
#            [4, 1, 2, 3]]

example = [[(i+j)%N for j in range(1, N+1)] for i in range(1, N+1)]

for i in range(N):
    for j in range(N):
        print(f'i, j: {i}, {j}')
        print(f'N의 배수 ? {example[i][j] - i - j + 1 + 2}\n')
