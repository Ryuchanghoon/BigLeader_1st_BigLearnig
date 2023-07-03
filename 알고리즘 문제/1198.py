import sys

input = sys.stdin.readline


def what(x1, y1, x2, y2, x3, y3):
    val = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)

    if val > 0:
        return 1 # 반시계
    
    elif val < 0:
        return -1 # 시계
    
    else:
        return 0 # 직선.


n = int(input())

points = []

for i in range(n):
    x, y = map(int, input().split())
    points.append([x,y])

res = 0

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if what(points[i][0], points[i][1], points[j][0], points[j][1], points[k][0], points[k][1]) == 0:
                continue
            area = 0.5 * abs(points[i][0] * points[j][1] + points[j][0] * points[k][1] + points[k][0] * points[i][1] - points[i][1] * points[j][0] - points[j][1] * points[k][0] - points[k][1] * points[i][0])
            res = max(res, area)


print(res)