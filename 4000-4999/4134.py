# 아니;; 누가 봐도 안되는데... 왜됌???
# 실버라 테스트 케이스를 널널하게 줬나?
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [int(input()) for _ in range(int(input()))]

for num in nums:
    if is_prime(num):
        print(num)
    else:
        while True:
            num += 1
            if is_prime(num):
                print(num)
                break