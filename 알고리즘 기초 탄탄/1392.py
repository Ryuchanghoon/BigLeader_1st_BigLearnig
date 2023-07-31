import sys

input = sys.stdin.readline

a, b = map(int,input().split())


list1 = []


for _ in range(a):
    x = int(input())
    list1.append(x)


for _ in range(b):
    x1 = int(input())
    time = 0


    for i,j in enumerate(list1):
        time += j

        if time -1 >= x1:
            print(i + 1)
            break