import sys
lst = [1, 1]
count = 1

x = int(sys.stdin.readline())
i = 1
while True:
    i += 1
    if count == x:
        break
    for j in range(i):
        if count == x:
            break
        if i % 2 == 0:
            count += 1
            if j == 0:
                lst[0] = 1
                lst[1] = i
            elif j > 1 and i in lst:
                break
            else:
                    lst[0] += 1
                    lst[1] -= 1
            
        else:
            count += 1
            if j == 0:
                lst[0] = i
                lst[1] = 1
            elif j > 1 and i in lst:
                break
            else:
                    lst[0] -= 1
                    lst[1] += 1
print("{}/{}".format(lst[0], lst[1]))