import sys

input = sys.stdin.readline


n = int(input())
peoples = []


for _ in range(n):
    wei, hei = map(int, input().split())
    peoples.append((wei, hei))


numbering = []  # 떡대 순위

for i in range(n):
    number = 1
    for j in range(n):
        if peoples[i][0] < peoples[j][0] and peoples[i][1] < peoples[j][1]:
            number += 1
    numbering.append(number)


print(*numbering) # 띄어쓰기 기준 분리.