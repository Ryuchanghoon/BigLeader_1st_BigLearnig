from itertools import permutations

def base_strike(ball, guess, n):
    strike = 0
    for i in range(n):
        if ball[i] == guess[i]:
            strike += 1
    return strike

def base_ball(ball, guess, n):
    ball = 0
    for i in range(n):
        if ball[i] in guess and ball[i] != guess[i]:
            ball += 1
    return ball

def solve():
    n = int(input())
    base = []
    for _ in range(n):
        a, b, c = map(int, input().split())
        base.append((str(a), b, c))

    possible_numbers = list(permutations([str(i) for i in range(1, 10)], 3))
    answer = 0

    for number in possible_numbers:
        is_possible = True

        for baseball in base:
            a, b, c = baseball
            ball = str(ball)

            if base_strike(ball, number, 3) != strike or base_ball(ball, number, 3) != ball_count:
                is_possible = False
                break

        if is_possible:
            answer += 1

    print(answer)


solution()