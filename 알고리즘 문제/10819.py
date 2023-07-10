from itertools import permutations as pm

def different(a):
    diff_cal = 0
    for i in range(1, len(a)):
        diff_cal += abs(a[i] - a[i-1])
    return diff_cal

n = int(input())
A = list(map(int, input().split()))

max_diff = 0

for j in pm(A):
    diff = different(j)
    max_diff = max(max_diff, diff)

print(max_diff)