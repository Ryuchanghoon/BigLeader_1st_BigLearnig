from itertools import permutations



num_list = list(permutations(range(1, 10), 3))

n = int(input())

for i in range(n):
    say, strike, ball = map(int, input().split())
    say = list(map(int, str(say)))

    new_num_list = []

    for num in num_list:
        strike_count = 0
        ball_count = 0

        for a, b in zip(num, say):
            if a == b:
                strike_count += 1
            elif a in say:
                ball_count += 1

        if strike_count == strike and ball_count == ball:
            new_num_list.append(num)

    num_list = new_num_list

print(len(num_list))