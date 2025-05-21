x, y, w, s = map(int, input().split())
if 2*w > s: print(min(x, y) * s + min(abs(x-y)//2*2*s + (abs(x-y)%2 * w), abs(x-y)*w))
else: print((x+y)*w)