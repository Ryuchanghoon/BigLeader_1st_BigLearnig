import sys

input = sys.stdin.readline

'''
x_list = []

n = int(input())


for _ in range(n):
    x = int(input().strip())
    x_list.append(x)

for i in x_list:
    dp = [0] * (i+1) # 0 배열 생성. dp[0,1,2] 크기 포함 위해 i+1
    dp[0] = 1 # 0 표현 방법 1가지
    dp[1] = 1 # 1 표현 방법 1가지
    dp[2] = 2 # 2 표현 방법 1+1 = 2 가지

    for j in range(3, i + 1): ####
        dp[j] = dp[j - 1] + dp[j - 2] + dp[j - 3] #####

    print(dp[i])

'''


for i in range(int(input())):
    n = int(input())
    dp = [0] * (n + 1)

    if n == 1:
        print(1)

    elif n == 2:
        print(2)

    elif n == 3:
        print(4)

    else:
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4

        for j in range(4, n + 1):
            dp[j] = dp[j-1] + dp[j-2] + dp[j-3]

        print(dp[n])