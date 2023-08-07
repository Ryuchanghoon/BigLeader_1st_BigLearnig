import sys

input = sys.stdin.readline

building = []

n = int(input())

for i in range(n):
    sky = tuple(map(int, input().split()))
    building.append(sky)

stack = [0]

change = 0

for _, height in building: ####
    
    while stack[-1] > height:
        stack.pop()
        change += 1
    
    if stack[-1] != height:
        stack.append(height)


change += len(stack) - 1



print(change)