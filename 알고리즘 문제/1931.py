import sys


input = sys.stdin.readline

n = int(input())
list_akk = []

for _ in range(n):
    a,b = map(int,input().split())
    list_akk.append((a,b))

list_akk(key = lambda x: x[1])

cnt = 1

end = list_akk[0][1]

for i in range(1, n):
    if list_akk[i][0] >= end:
        cnt += 1

        end = list_akk[i][1]

print(cnt)