n = int(input())
lst = []
lst2 = []
lst3 = []

for i in range(n):
    lst += [list(map(int, input().split()))]

for i in range(len(lst)):
    lst2.append(lst[i][0])
    lst3.append(lst[i][1]) 

lst2.sort()
lst3.sort()

num = (lst2[-1] - lst2[1]) - (lst2[1] - lst2[0])

num2 = (lst3[-1] - lst3[0])

result = num * num2

print((100*n) - (result))