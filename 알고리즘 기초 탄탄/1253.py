import sys

input = sys.stdin.readline

n = int(input())

a_i = list(map(int, input().split()))

a_i.sort()

count = 0



for i in range(n):
    target = a_i[i]
    others = a_i[:i] + a_i[i+1:]
    left, right = 0, len(others) - 1

    while left < right:
        current_sum = others[left] + others[right]
        
        if current_sum == target:
            count += 1
            break

        elif current_sum < target:
            left += 1
        
        else:
            right -= 1

print(count)