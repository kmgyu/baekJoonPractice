def multMul(m1, m2):
    ans = []
    for i in range(len(m1)): # m1의 행
        row = []
        for j in range(len(m2[0])): # m2의 열
            sum = 0
            for k in range(len(m1[0])):
                sum += m1[i][k] * m2[k][j] # m1의 열과 m2의 행
            row.append(sum) # 각 원소를 행에 넣어주기
        ans.append(row) # 행을 결과에 넣어주기
    return ans  #결과 반환!

def powerMat(x, n): # 알고리즘 4.9 행렬 거듭 제곱 알고리즘
    if n == 1: return x
    elif n&1 == 0:
        return powerMat(multMul(x, x), n//2)
    else:
        # multMul() 썼다!
        return multMul(x, powerMat(multMul(x, x), (n-1)//2))

def testing(mat, n):
    print(*powerMat(mat, n), sep="\n")
    print() # 여백의 미


# test drivers
mat1 = [[1, 2], [3, 4]]
mat2 = [[5, 6], [7, 8]]
mat3 = [[3]]
mat4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 

testing(mat1, 2) # 답 : [7, 10], [15, 22]
testing(mat2, 3) # 답 : [881, 1026], [1197, 1394]
testing(mat3, 4) # 답 : [81]
testing(mat4, 2) # 답 : [30, 36, 42], [66, 81, 96], [102, 126, 150]