import sys
from collections import deque


input = sys.stdin.readline

'''
n, k = map(int, input().split())

time = 0

while n != k:
    
    if k < n:
        n -= 1
    
    else:
        n += 1

    time += 1  


print(time)
'''



n, k = map(int,input().split())


queue = deque([(n, 0)])
visit = set([n])

while queue:
    now, time = queue.popleft()

    if now == k:
        print(time)
        break

    for next in [now + 1, now-1]:
        if 0 <= next <= 100000 and next not in visit:
            visit.add(next)
            queue.append((next, time + 1))