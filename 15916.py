n = int(input())
nums = list(map(int, input().split()))
k = int(input())

f = []
ans = 0

if k - nums[0] == 0:
    print("T")
    exit()
elif k - nums[0] < 0:
    for i in range(1, n+1):
        if k*i-nums[i-1] >= 0:
            print("T")
            exit()
else:
    for i in range(1, n+1):
        if k*i-nums[i-1] <= 0:
            print("T")
            exit()
print("F")


# https://justicehui.github.io/sunrin-ps/2018/09/14/BOJ15916/
# https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=chogahui05&logNo=221324025625