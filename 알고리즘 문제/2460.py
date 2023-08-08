import sys

input = sys.stdin.readline

in_train = 0
max_per = 0

for i in range(10):
    a,b = map(int, input().split())
    in_train = in_train - a + b
    
    max_per = max(max_per, in_train)


print(max_per)