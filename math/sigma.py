import sys

input = sys.stdin.readline
print = sys.stdout.write

a, b = map(int, input().split())
print(str(int((a + b)/2 * (abs(b-a)+1)))+"\n")