import math
import sys

input = sys.stdin.readline

for i in range(int(input())):

    x,y = map(int,input().split())
    
    dist = y - x

    sqrt_dis = math.isqrt(dist)
    
    if sqrt_dis ** 2 == dist:
        jump = 2 * sqrt_dis - 1


    else:

        #sqrt_dis = math.isqrt(dist)
        sqrt_dis_remain = dist - sqrt_dis ** 2
        jump = 2 * sqrt_dis

        if sqrt_dis_remain > sqrt_dis:
            jump += 1

    print(jump)