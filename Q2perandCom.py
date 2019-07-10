from itertools import combinations
num ,y = input().split()
b = int(y)
number = []
g = combinations(num,len(num)-b)
for i in g:
    number.append("".join(i))
print(min(number))
