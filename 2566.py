result = []
result2 = []

for i in range(9):
    lst = []
    lst += list(map(int, input().split()))
    lst2 = sorted(lst)
    
    result.append(lst2[-1])
    result2.append(lst.index(lst2[-1])+1)

lst2 = sorted(result)

print(lst2[-1])
print(result.index(lst2[-1])+1,result2[result.index(lst2[-1])])