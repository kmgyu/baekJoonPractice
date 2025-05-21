def solve(dist, center, x, y, mod):
    # print(dist, center)
    left = (dist-center)//2
    right = (dist+center)//2
    
    if left <= x < right and left <= y < right: # in center
        return 1
    if dist == N or mod == 0: # end of recur
        # print(x, y, left, right, dist, center)
        return 0
    # make it minimize
    # modular 연산 시 셀단위를 N에서 1로 축소하는 효과를 낸다.
    # 회귀한다고 생각하면 됨 그냥. 이거 글로 설명하기 으렵다

    return solve(dist//N, center//N, x%mod, y%mod, mod//N)

s, N, K, R1, R2, C1, C2 = map(int, input().split())

dist = N**s # N * N**(s-1)
center = K*(N**(s-1))
modular = N**(s-1)

for i in range(R1, R2+1):
    line = [solve(dist, center, i, j, modular) for j in range(C1, C2+1)]
    print(*line, sep='')