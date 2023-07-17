import sys

input = sys.stdin.readline

a, b = map(int, input().split())
    
row_1, col_1 = divmod(a - 1, 4) # divmod가 몫 나머지 연산 한방에.
    
row_2, col_2 = divmod(b - 1, 4)
    
    
col = abs(col_2 - col_1)
row = abs(row_2 - row_1)


dist = col + row
    
print(dist)
