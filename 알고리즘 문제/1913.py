import sys

input = sys.stdin.readline

n = int(input())

what = int(input())


snail = [[0] * n for _ in range(n)] # matrix 생성

x, y = -1, 0 # 현재 위치
dir = 1 # 이동 방향


num = n ** 2



while num > 0:

    # X 축
    for i in range(n): # 숫자 가득 채우고
        x += dir # 방향(dir)만큼 증가.
        snail[y][x] = num
        num -= 1 # 달팽이 움직이고  1개씩 감소.
    
    # Y 축. 위랑 동일.
    for j in range(n - 1):
        y += dir
        snail[y][x] = num
        num -= 1
        
    dir = -dir
    n -= 1


for i in range(len(snail)):
    for j in range(len(snail)):
        if snail[i][j] == what:
            print(i+1, j+1)
        print(snail[i][j], end=' ')
    print()