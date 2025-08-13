# CCW
# https://velog.io/@skyepodium/%EA%B8%B0%ED%95%98-CCW-tojy2dp4z8
# https://snowfleur.tistory.com/98
# CCW + CCW를 이용한 선분교차판별
# https://jason9319.tistory.com/358
# 3개의 점 A,B,C에 대해 점 3개를 이은 방향을 알고자할 때 이용
# '기하' 알고리즘이다.
# 행렬을 통해 벡터 외적을 얻어 시계, 반시계, 직선 방향을 판단함.
# CCW를 이용했는데 1, -1이 나오면 두 선분 사이 어딘가에 있다는 뜻.
# 두개 다 -1이면 두 선분이 교차한다...!
# 0일때는 평행하거나 겹치는 경우이다. 벡터라고 보면 겹치는 경우라고 할 수 있을듯?
# 음... 설명할 수준은 아닌듯...

# CCW
def ccw(a, b, c):
    ans = a[0]*b[1] + b[0]*c[1] + c[0]*a[1]
    ans -= a[1]*b[0] + b[1]*c[0] + c[1]*a[0]
    if ans > 0: return 1 # 반시계
    elif ans < 0: return -1 # 시계
    else: return 0 # 평행

# 선분 교차 판정 (return : boolean)
def isIntersect(l1, l2):
    a, b = l1
    c, d = l2
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab == 0 and cd == 0:
        if a > b: a,b=b,a
        if c > d: c,d=d,c
        return c <= b and a <= d
    return ab <= 0 and cd <= 0
