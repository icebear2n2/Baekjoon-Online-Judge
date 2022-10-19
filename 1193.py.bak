lst2 = [1, 1]
count = 1
x = int(input())
k = 2
while True:
    if count == x:
        break
    lst = [ 0 for i in range(k) ]
    
    if k % 2 == 0:
        for i in range(len(lst)+1):
            if count == x:
                break
            if i == 0:
                count += 1
                lst2[0] = 1
                lst2[1] = len(lst)
            elif i > 1 and len(lst) in lst2:
                num = lst2
                break
            else:
                count += 1
                lst2[0] += 1
                lst2[1] -= 1
    else:
        for i in range(len(lst)+1):
            if count == x:
                break
            if i == 0:
                count += 1
                lst2[0] = len(lst)
                lst2[1] = 1
            elif i > 1 and len(lst) in lst2:
                num = lst2
                break
            else:
                count += 1
                lst2[0] -= 1
                lst2[1] += 1
    k+=1

print("{}/{}".format(lst2[0], lst2[1]))