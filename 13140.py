from itertools import permutations
from sys import stdin
input = stdin.readline

n = int(input().strip())

for s in permutations(range(10), 7):
    h, e, l, o, w, r, d = s
    word_hello = 10000 * h + 1000 * e + 100 * l + 10 * l + o
    word_world = 10000 * w + 1000 * o + 100 * r + 10 * l + d
    if word_hello + word_world == n and h != 0 and w != 0:
        print(f"  {word_hello}")
        print(f"+ {word_world}")
        print("-------")
        print(f"{n:7}")
        exit()
print("No Answer")