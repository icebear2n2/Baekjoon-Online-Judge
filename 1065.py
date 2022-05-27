import sys

n = int(sys.stdin.readline())
num=0
lst = list()
for i in range(1, n+1):
    
    if i >= 10 and i < 100:
        i=str(i)
        for j in range(1, int(len(str(n))) + 1):
            result=int(i[j]) - int(i[j-1])
            lst.append(result)
                
        if len(set(lst)) == 1:
            num+=1
            lst.clear()
        else:
            continue
    elif i >= 100 and i < 1000:
        i=str(i)
        for j in range(1, len(str(n)) + 1):
            lst.append(int(i[j]) - int(i[j-1]))
                
        if len(set(lst)) == 1:
            num+=1
            lst.clear()
        else:
            continue
    else:
        num += 1
        lst.clear()
    
print(num)
