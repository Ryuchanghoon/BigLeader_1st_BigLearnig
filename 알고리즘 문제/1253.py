import sys

input = sys.stdin.readline

n = int(input())

a_i = list(map(int, input().split()))


count = 0



for i in range(n):
    target = a_i[i]
    others = a_i[:i] + a_i[i+1:]
    left, right = 0, len(others) - 1

    while left < right:
        sum = others[left] + others[right]
        
        if sum == target:
            count += 1
            break

        elif sum < target:
            left += 1
        
        else:
            right -= 1

print(count)