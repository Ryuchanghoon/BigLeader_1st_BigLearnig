import sys
import math

input = sys.stdin.readline


for i in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    
    ds = math.sqrt((x2 - x1) ** 2 + (y2 - y1)**2)
    sum = r1 + r2
    diff = abs(r1 - r2)

    if ds == 0:
        if r1 == r2:
            print(-1)

        else:
            print(0)

    else:
        if sum < ds or ds < diff:
            print(0)

        elif sum == ds or ds == diff:
            print(1)

        else:
            print(2)