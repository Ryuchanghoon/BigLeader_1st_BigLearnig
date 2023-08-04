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



def bfs(a, b):
    queue = deque([(a, 0)])
    visit = set([a])

    while queue:
        now, time = queue.popleft()

        if now == b:
            return time

        for next in [now + 1, now - 1, now * 2]:
            if 0 <= next <= 100000 and next not in visit:
                visit.add(next)
                queue.append((next, time + 1))

n, k = map(int, input().split())
result = bfs(n, k)
print(result)