import sys

input = sys.stdin.readline

a = input()

count = 0

for i in range(len(a) + 1):
    x = input()
    if x[i] != x[i + 1] and x[i + 1] != x[i + 2] and x[i] != x[i + 2]:
        count += 1

print(count)