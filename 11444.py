#행렬곱을 이용한 고속 피보나치 계산

def mul(A, B):
    ans = [[0]*2 for _ in range(2)]
    for row in range(2):
        for col in range(2):
            e = 0
            for i in range(2):
                e += A[row][i] * B[i][col]
            ans[row][col] = e % mod
    
    return ans

def pow(A, k):
    if k == 1:
        return A
    
    matrix = pow(A, k//2)
    if k % 2:
        return mul(mul(matrix, matrix), A)
    else:
        return mul(matrix, matrix)

matrix = [[0, 1], [1, 1]]

n = int(input())
mod = 1000000007
ans = [[0]*2 for _ in range(2)]

matrix = pow(matrix, n)

print(matrix[1][0])
