num=int(input())
for i in range(num):
    k = int(input())
    x = int(input())

    lst = [i for i in range(1, x+1)]
    lst2 = [i for i in range(1, x+1)]

    for n in range(k):
        for i in range(len(lst)):
            for j in range(i):
                lst2[i] += lst[j]

        lst.clear()
        lst.extend(lst2)
    print(lst2[x-1])

