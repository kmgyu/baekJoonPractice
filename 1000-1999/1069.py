# 이등변 삼각형
# 케이스가 생각보다 많았음.
# 총 6개...?
# case 1: 걷기
# case 2: dist 방향 점프 + 걷기
# case 3: 삼각형을 이용. D*2보다 작은 변을 가진 삼각형은 존재한다.
# 거기서 이득을 취하는 걸 짜면 되는데... 하다가 실패함! 복잡하게 짰다가 실패햇당ㅎ

X, Y, D, T = map(int, input().split())
dist = (X**2 + Y**2)**0.5
jump = dist//D

if dist > D:
    case1 = T * jump + (dist - (D * jump))
    case2 = dist
    case3 = T * (jump + 1)
    
    result = min(case1, case2, case3)
    result = round(result,9)
    print(result)
else:
    case1 = T + (D - dist)
    case2 = dist
    case3 = T * 2
    
    result = min(case1, case2, case3)
    result = round(result,9)
    print(result)
    
    
    
# 아까워서 남김
# import math

# X, Y, D, T = map(int, input().split())
# dist = math.dist((X, Y), (0, 0))
# ans = 0

# if D > T:
#     jump = dist//D
#     ans = jump * T
#     dist -= D * jump
    
#     if jump == 0:
#         ans = dist
#         dist = 0


# if dist > 0:
#     # 삼각형 특 : D * 2 > dist 면 삼각형임
#     # 각도는 생각할 필요 없고, 직선으로 이동하는 게 이득인지 체크하면 된다.
#     # 직선 vs 삼각형
#     if ans > 0 and (T > T+D-dist): ans += dist*2 - D
#     else: ans += T

# print(ans)