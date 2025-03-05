input = open(0).readline

s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

lcs_list = [[[0] * (len(s1)+1) for _ in range(len(s2)+1)] for _ in range(len(s3)+1)]

# 9251 reference

for i in range(len(s1)):
    for j in range(len(s2)):
        for k in range(len(s3)):
            if s1[i] == s2[j] == s3[k]:
                lcs_list[k+1][j+1][i+1] = lcs_list[k][j][i] + 1
            else:
                lcs_list[k+1][j+1][i+1] = max(lcs_list[k+1][j][i], lcs_list[k][j+1][i], lcs_list[k][j][i+1],
                                              lcs_list[k+1][j+1][i], lcs_list[k][j+1][i+1], lcs_list[k+1][j][i+1])

print(lcs_list[-1][-1][-1])