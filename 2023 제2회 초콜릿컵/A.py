import sys
input = sys.stdin.readline

def rev(s):
    return s[::-1]
def head(s):
    l = (len(s)+2)//3
    return s[:l]
def tail(s):
    return s[1:]
def ice(s):
    ss = head(s)
    sr = rev(ss)
    st = tail(ss)
    if s == ss + sr + ss:
        return 1
    elif s == ss + tail(sr) + ss:
        return 1
    elif s == ss + sr + st:
        return 1
    elif s == ss + tail(sr) + st:
        return 1
    return 0


t = int(input())
for i in range(t):
    print(ice(input().rstrip()))

