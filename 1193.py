lst2 = [1, 1]
count = 2

for k in range(2, 6):

    lst = [ 0 for i in range(k) ]
    
    if k % 2 == 0:
        for i in range(len(lst)+1):
            if i == 0:
                lst2[0] = 1
                lst2[1] = len(lst)
                print(count)
                print(lst2)
                count+=1
            elif i > 1 and len(lst) in lst2:
                num = lst2
                break
            else:
                lst2[0] += 1
                lst2[1] -= 1
                print(count)
                print(lst2)
                count+=1
    else:
        for i in range(len(lst)+1):
            if i == 0:
                lst2[0] = len(lst)
                lst2[1] = 1
                print(count)
                print(lst2)
                count+=1
                
                
            elif i > 1 and len(lst) in lst2:
                num = lst2
                break
            else:
                lst2[0] -= 1
                lst2[1] += 1
                print(count)
                print(lst2)
                count+=1
