count = 1

x = int(input())
i = 1
lst = [1,1]
while True:
    i+=1
    if count == x:
        break
    for j in range(i):
        if count == x:
            break
        count += 1
        if i % 2 == 0:
            if j == 0:
                lst[0] = 1
                lst[1] = i
            else:
                lst[0] += 1
                lst[1] -= 1
        else:
            if j == 0:
                lst[0] = i
                lst[1] = 1
            else:
                lst[0] -= 1
                lst[1] += 1
print("{}/{}".format(lst[0], lst[1]))