import sys

input = sys.stdin.readline

n, m = map(int, input().split())
gong = list(range(n + 1))
what = [list(map(int, input().split())) for _ in range(m)]


for x in what:
    i, j = x
    gong[i], gong[j] = gong[j], gong[i]

print(*gong[1:])