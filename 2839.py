# 3, 5
# 18, 4, 6, 9, 11
n = int(input())

if (n - 3) == 0 or (n - 5) == 0:
    print(1)
else:
    while True:
        if n % 5 == 3:
            print((n // 5)+1)
            break
        else:
            if n % 3 == 0:
                print(n // 3)
            break