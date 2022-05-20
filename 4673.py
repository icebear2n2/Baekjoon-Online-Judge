m = list(range(1, 101))
n = 1
num = 1
while True:
    if n < 10:
            n+=n
            print(n)
            m.remove(n)
    else:
        n = n + (n // 10) + (n % 10)
        print(n)
        if n < 100:
            m.remove(n)
        else:
            break
print(m)