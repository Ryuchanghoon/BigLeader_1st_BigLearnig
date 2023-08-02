import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

queue = deque()

for i in range(n):
    insert = input().strip().split()

    if insert[0] == 'push':
        queue.append(int(insert[1]))

    elif insert[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    elif insert[0] == 'size':
        print(len(queue))
    
    elif insert[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
        
    elif insert[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
        
    elif insert[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)