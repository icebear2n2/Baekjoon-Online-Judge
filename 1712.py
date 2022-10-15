from fractions import Fraction

a, b, c = map(int, input().split())

num = a // (1 - Fraction(b, c))

i = num // c

if (a + (b * 2100000000)) > (c * 2100000000):
    print(-1)
elif num == (a + (b * i)):
    print(i+1) 
else:
    print(i)