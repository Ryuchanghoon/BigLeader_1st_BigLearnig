
str = input().split('-')
str_re = sum(map(int, str[0].split('+')))

for i in str[1:]:
    str_re -= sum(map(int,i.split('+')))


print(str_re)