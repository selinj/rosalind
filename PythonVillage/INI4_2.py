#given 2 integers, 0 < a < b < 10000
#return sum of all odd integers from a through b, inclusively

sum = 0

a = 4008
b = 8576

for i in range(a,b+1):
    if i % 2 == 1: #then odd
        sum = sum + i

print sum
