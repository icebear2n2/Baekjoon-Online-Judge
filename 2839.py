# 3, 5
# 18, 4, 6, 9, 11

n = int(input())

num1 = 3
num2 = 5

if n % 8 == 0:
    print((n // 8) * 2)
elif n % 8 == num1 or  n % 8 == num2:
    print(((n // 8) * 2) + 1)
else:
    if n % num1 == 0:
        print(n // num1)
    elif n % num2 == 0:
        print(n // num2)
    else:
        print(-1)