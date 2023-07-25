import sys

input = sys.stdin.readline

n = int(input())

list = [0,1]

for i in range(2, n+1):
    list.append(list[-1] + list[-2])
    
print(list[n])