lst = []
while True:
    x = int(input())
    lst.append(x)
    if len(lst) == 28:
        break

lst.sort()


for i in range(1, 31):
    if i not in lst:
        print(i)