import sys
def input(): return sys.stdin.readline().rstrip()

w, h = map(int, input().split())
print("%.1f" % (w*h * 0.5))