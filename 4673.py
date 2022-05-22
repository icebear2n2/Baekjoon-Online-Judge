lst = list()
lst1 = list(range(1, 10001))
n = 1

# 1
while True:
    if n < 10:
        n+=n 
        lst.append(n)
    elif n >= 10 and n < 100:
        n = n + (n // 10) + (n % 10)
        lst.append(n)
    elif n >= 100 and n < 1000:
        n = n + (n // 100) + ((n // 10) % 10) + (n % 10)
        lst.append(n)
    elif n >= 1000 and n < 10000:
        n = n + (n // 1000) + ((n // 100) % 10) + ((n // 10) % 10) + (n % 10)
        lst.append(n)
    else:
        break

# 2
for i in range(1, 10001):
    if i < 10:
        i+=i
        lst.append(i)
    elif i >= 10 and i < 100:
        i = i + (i // 10) + (i % 10)
        lst.append(i)
    elif i >= 100 and i < 1000:
        i = i + (i // 100) + ((i // 10) % 10) + (i % 10)
        lst.append(i)
    elif i >= 1000 and i < 10000:
        i = i + (i // 1000) + ((i // 100) % 10) + ((i // 10) % 10) + (i % 10)
        lst.append(i)
    else:
        break

for i in set(lst):
    if i in lst1:
        lst1.remove(i)
    else:
        continue

for i in lst1:
    print(i)

