lst = [1, 2, 3]
lst2 = [1, 2, 3]

for i in range(len(lst)):
    print(i)
    for j in range(i):
        lst2[i] += lst[j]
        print(lst2)


lst.clear()

lst.extend(lst2)

