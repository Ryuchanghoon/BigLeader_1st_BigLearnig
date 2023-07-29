from itertools import combinations

def Lotty():
    while True:
        
        lotty_list = input().split()
        
        if lotty_list[0] == '0':
            break


        lotto = list(map(int, lotty_list[1:]))

        for i in combinations(lotto, 6):
            print(*i)

        print()

Lotty()