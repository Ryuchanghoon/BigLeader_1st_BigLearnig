import sys

input = sys.stdin.readlines

n = int(input())
s = input().strip()


q = [(0, 0)]  # 스ㅏ트
d_r = [0, 1, 0, -1]  # r 방향
d_c = [1, 0, -1, 0]  # c 방향 리스트
dir = 0  # 0 -> x+, 1 -> y-, 2 -> x-, 3 -> y+
max_r = 0
min_r = 0
max_c = 0
min_c = 0


for c in s:
    if c == 'R':
        dir = (dir + 1) % 4

    elif c == 'L':
        dir = (dir - 1) % 4

    else:
        q.append((q[-1][0] + d_r[dir], q[-1][1] + d_c[dir]))
        max_r = max(max_r, q[-1][0])
        max_c = max(max_c, q[-1][1])
        min_r = min(min_r, q[-1][0])
        min_c = min(min_c, q[-1][1])

field = [['#' for i in range(min_c, max_c + 1)] for j in range(min_r, max_r + 1)]
# 최소 최대 예

for r, c in q:
    row, col = r - min_r, c - min_c
    field[row][col] = '.'

for row in field:
    print(''.join(row))