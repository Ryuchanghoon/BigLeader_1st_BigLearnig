import sys

input = sys.stdin.readline

a = int(input())

for i in range(a):
    for j in range(i+1):
        print("*", end="")

    for j in range(2*(a-i-1)):
        print(" ", end="")

    for j in range(i+1):
        print("*", end="")
    print()

for i in range(a-1, 0, -1):
    for j in range(i):
        print("*", end="")

    for j in range(2*(a-i)):
        print(" ", end="")
        
    for j in range(i):
        print("*", end="")
    print()


# 눈 아프다